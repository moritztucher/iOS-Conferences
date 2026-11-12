#!/usr/bin/env bash
# Runs the data checks against a pull request before you merge it. GitHub Actions
# no longer validates PRs, so this is the gate for contributor PRs.
#
#     scripts/check_pr.sh 12
#
# The PR is checked out into a throwaway worktree, so your own checkout and any
# uncommitted work in it are never touched. Needs the GitHub CLI (`gh`).
set -euo pipefail

if [[ $# -ne 1 || ! $1 =~ ^[0-9]+$ ]]; then
  echo "Usage: scripts/check_pr.sh <pr-number>" >&2
  exit 2
fi

root=$(git rev-parse --show-toplevel)
cd "$root"
pr=$1
ref="refs/check-pr/$pr"
dir=$(mktemp -d)
trap 'cd "$root"; git worktree remove --force "$dir" >/dev/null 2>&1 || true; git update-ref -d "$ref"' EXIT

git fetch --quiet origin main "pull/$pr/head:$ref"
git worktree add --quiet --detach "$dir" "$ref"

# The checks run main's scripts against the PR's data, never the PR's own scripts:
# running them would execute a stranger's code on this machine. A PR that changes
# scripts/ needs reading by hand.
if ! git diff --quiet origin/main..."$ref" -- scripts; then
  echo "PR #$pr changes scripts/ — review those changes by hand; checking with main's scripts."
fi
rm -rf "$dir/scripts"
git archive origin/main scripts | tar -x -C "$dir"

# -I keeps Python from importing modules out of the PR's tree.
cd "$dir"
python3 -I scripts/validate_conferences.py
python3 -I scripts/validate_schedules.py
python3 -I scripts/generate_readme.py --check
echo "PR #$pr: all checks passed."
