# iOS Conferences

An open, community-curated list of iOS / Apple-platform developer conferences and the events around them: meetups, WWDC watch parties, hack days, and more, sorted by date.

This repository is the data behind **[dubdub - Conferences & Events](https://apps.apple.com/app/id6774134161)** for iPhone and iPad. The list below shows this year's and upcoming conferences from [`data/conferences.json`](./data/conferences.json) and updates itself whenever the data changes. Earlier years, meetups, watch parties, and other events are in the JSON and the app.

## Contributing

Spotted a missing conference, a wrong date, or a cancelled event? Any of these works:

- **In the app:** Settings → **Suggest a conference**. Fill in the form and send it as an email or a pre-filled GitHub issue.
- **GitHub issue:** [open a conference request](https://github.com/moritztucher/iOS-Conferences/issues/new?template=conference-request.yml).
- **Pull request:** edit [`data/conferences.json`](./data/conferences.json) directly. The schema and the rules for what gets listed are in [CONTRIBUTING.md](./CONTRIBUTING.md).

## Conferences

<!-- conferences:start -->

### 2026

| Date | Conference | Location |
| --- | --- | --- |
| 21–23 Jan 2026 | [iOS Conf SG 2026](https://www.iosconf.sg) | Singapore |
| 28–29 Mar 2026 | [LET'S VISION 2026](https://letsvision.swiftgg.team) | Shanghai, China |
| 12–14 Apr 2026 | [Deep Dish Swift 2026](https://deepdishswift.com) | Rosemont, Illinois, USA |
| 12–14 Apr 2026 | [try! Swift Tokyo](https://tryswift.jp) | Tokyo, Japan |
| 4–6 May 2026 | [iOSKonf26](https://ioskonf.mk) | Skopje, North Macedonia |
| 18–20 May 2026 | [Swift Craft 2026](https://swiftcraft.uk) | Folkestone, United Kingdom |
| 7–12 Jun 2026 | [CommunityKit](https://communitykit.social) | Cupertino, California, USA |
| 8–12 Jun 2026 | [WWDC 2026](https://developer.apple.com/wwdc/) | Cupertino, California, USA |
| 4–5 Jul 2026 | [Swift Conf Indonesia](https://events.zoom.us/ev/Ak7afLpOD12YzGD6W7z7zK-IrFm7lDceLyIglo8w-3cRnUybn-Gx~AvM1tOkv4U-EKGtEOoFGFJWrVcYfYZk70b_UgNe0RMu9zKMvMHJGD-T70Q) | Jakarta, Indonesia |
| 7–10 Jul 2026 | [MacAdmins Conference 2026](https://macadmins.psu.edu/) | State College, USA |
| 22–23 Jul 2026 | [Swift Rockies](https://swiftrockies.com) | Calgary, Alberta, Canada |
| 25–26 Jul 2026 | [iPlayground 2026](https://iplayground.io/2026/) | Taipei, Taiwan |
| 7–10 Sep 2026 | [iOSDevUK](https://www.iosdevuk.com) | Aberystwyth, UK |
| 7–11 Sep 2026 | [Swift Island](https://swiftisland.nl) | Texel, Netherlands |
| 16–18 Sep 2026 | [NSSpain XIV](https://2026.nsspain.com) | Logroño, Spain |
| 29 Sep – 2 Oct 2026 | [MacSysAdmin 2026](https://www.macsysadmin.se) | Gothenburg, Sweden |
| 7–9 Oct 2026 | [swiftCon Berlin 2026](https://www.nextappcon.com/swiftcon) | Berlin, Germany |
| 13–14 Oct 2026 | [SwiftLeeds](https://swiftleeds.co.uk) | Leeds, UK |
| 21–22 Oct 2026 | [Mobius 2026 Autumn](https://mobiusconf.com/en/) | Saint Petersburg, Russia |
| 2–3 Nov 2026 | [Swift Connection X](https://swiftconnection.io) | Paris, France |
| 10–12 Nov 2026 | [Do iOS 2026](https://do-ios.com) | Amsterdam, Netherlands |
| 19–20 Nov 2026 | [Swift Bharat 2026](https://www.swiftbharat.org) | Mumbai, India |
| 20–22 Nov 2026 | [Swiftsonic '26](https://swiftsonicconf.com) | Nashville, Tennessee, USA |

### 2027

| Date | Conference | Location |
| --- | --- | --- |
| 20–22 Jan 2027 | [iOS Conf SG 2027](https://2027.iosconf.sg) | Singapore |
| 2–4 Feb 2027 | [Arctic Conference 2027](https://arcticonference.com) | Oulu, Finland |
| 2–4 Mar 2027 | [try! Swift Tokyo 2027](https://tryswift.jp) | Tokyo, Japan |
| 17–20 Mar 2027 | [Appdevcon 2027](https://appdevcon.nl) | Amsterdam, Netherlands |
| 4–6 Apr 2027 | [Deep Dish Swift 2027](https://deepdishswift.com) | Rosemont, Illinois, USA |
| 6–9 Sep 2027 | [iOSDevUK 2027](https://iosdevuk.com/) | Aberystwyth University, Aberystwyth, Wales, UK |
| 29 Sep – 1 Oct 2027 | [swiftCon Berlin 2027](https://www.nextappcon.com/swiftcon) | Berlin, Germany |

<!-- conferences:end -->

## Using the data

The data is free to reuse under [CC BY 4.0](#license). Both files are plain JSON:

| File | URL |
| --- | --- |
| Conference list | `https://cdn.jsdelivr.net/gh/moritztucher/iOS-Conferences@main/data/conferences.json` |
| Talk schedule | `https://cdn.jsdelivr.net/gh/moritztucher/iOS-Conferences@main/data/schedules/<conference-id>.json` |

`raw.githubusercontent.com/moritztucher/iOS-Conferences/main/...` works as a fallback. The schema for both files is documented in [CONTRIBUTING.md](./CONTRIBUTING.md). Field names and conference ids are stable, because the app depends on them too.

## Policies

- [Privacy Policy](./PRIVACY.md)
- Terms of Use: the app uses Apple's [Standard End User License Agreement](https://www.apple.com/legal/internet-services/itunes/dev/stdeula/).

Questions or app feedback: [open an issue](https://github.com/moritztucher/iOS-Conferences/issues/new) or email **moritztucher@gmail.com**.

## License

The conference data in this repository (`data/`) is licensed under [**Creative Commons Attribution 4.0 International (CC BY 4.0)**](./LICENSE). You can copy, adapt, and use it for any purpose, including commercially, as long as you give credit:

> Conference data from [iOS Conferences](https://github.com/moritztucher/iOS-Conferences) (dubdub), CC BY 4.0.

Two exceptions:

- **Talk descriptions** (`description` in `data/schedules/*.json`) belong to the speakers and organisers who published them. They're imported from the organisers' own schedule feeds and aren't covered by this license.
- **The scripts in `scripts/`** are MIT-licensed. See [`scripts/LICENSE`](./scripts/LICENSE).

**Logos.** Conference logos are only displayed with the organiser's explicit permission. If you run a conference and would like your logo to appear next to your listing, either email the developer or open a PR with the image file. Logos remain the property of their respective owners and are used by permission only.

## Legal bits

This is a community project. It is not an Apple initiative and is not endorsed by, affiliated with, or sponsored by Apple Inc.

Apple, the Apple logo, App Store, iPhone, iPad, iOS, iPadOS, macOS, watchOS, tvOS, visionOS, Swift, the Swift logo, Xcode, and SF Symbols are trademarks of Apple Inc., registered in the U.S. and other countries.

Conference and event names, brands, and content link to their respective organisers. They appear in this list as factual references. We don't endorse, sponsor, sell, or take a cut of ticket sales. If you spot something that shouldn't be here (wrong info, a takedown request, anything else), [open an issue](https://github.com/moritztucher/iOS-Conferences/issues/new) or email **moritztucher@gmail.com**.

## Acknowledgements

The iOS developer community keeps putting on the most welcoming conferences in software. Most of them are run by volunteers. If you can attend one, do.

A particular nod to [**twostraws/wwdc**](https://github.com/twostraws/wwdc) by Paul Hudson and contributors, the source of much of the WWDC-week event data.
