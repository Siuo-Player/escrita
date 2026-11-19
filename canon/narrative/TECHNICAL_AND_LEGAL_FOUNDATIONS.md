# Technical and Legal Foundations (2009 Period-Accuracy)

Status: RESEARCHED CANONICAL REFERENCE — distinguish documented facts from narrative choices  
Updated: 2026-11-19

This document is a continuity aid, not legal, tax, or engineering advice. A source-backed historical fact should not be confused with a fictional decision about the Callahan family.

---

## 1. Apple Developer Program: legal and contractual model

### 1.1 Two different agreements must not be conflated

The March 2009 **Registered iPhone Developer Agreement** and the paid **iPhone Developer Program License Agreement** are different documents with different purposes.

- The Registered iPhone Developer Agreement filed as an exhibit in March 2009 says the account holder certifies that they are of legal age of majority. It then expressly allows a parent or legal guardian to let a person aged 13 through the age of majority share the parent's Apple ID and password **solely under the parent's supervision**. The parent remains responsible for that person's compliance with the agreement. This is the clearest contemporaneous basis for Nathan, aged 13, to participate through a parent's account; it does **not** mean Nathan could independently sign up as the contracting account holder. [Source A]
- The iPhone Developer Program License Agreement copy cited below carries revision date **17 March 2009**. It requires the contracting party to be of legal age, or to have authority to bind the company/organization on whose behalf the agreement is accepted. It also makes the account holder responsible for the activities and compliance of authorized developers. [Source B]
- App Store distribution required Apple to select and digitally sign the application. Distribution of a **paid** application required a separate agreement, identified as **Schedule 2**. The main Program Agreement alone was not sufficient to sell a paid app. The separate Schedule 2 terms are not included in the archived copy linked below, so this document does not invent their full payment, banking, or tax mechanics. [Source B]

### 1.2 Canonical arrangement for Nathan

For the existing story, the least complicated arrangement consistent with the located documents is:

1. **Clifford is the named adult account holder and contracting party.** Choose one identity for the account: a personal individual membership, or a company membership entered into by someone with authority to bind that company. Do not describe it as an “individual/enterprise” hybrid.
2. **Nathan is the 13-year-old author working under direct parental supervision.** He is not described as an independent Apple contracting account holder. The March 2009 Registered iPhone Developer terms provide a basis for supervised use of the parent's credentials by a 13+ minor, subject to the separate Program Agreement and its requirements.
3. **Clifford completes the paid-app paperwork as account holder.** The story must establish that the separate paid-app agreement was accepted before the $0.99 release. Apple review and selection still apply.
4. **Keep authorship and distribution distinct.** Nathan can be the programmer, designer, and credited creator while Clifford is the adult publisher/account holder shown in the Apple relationship. The family should explicitly decide who owns or controls the rights that Clifford must grant to Apple; do not imply that the developer agreement itself transfers Nathan's copyright to Clifford.
5. **Do not hard-code an automatic UTMA payout.** The sources located do not establish that Apple paid a minor directly, that a UTMA account was mandatory, or that an account could simply be “co-signed” by both parents. The earlier statement that sales revenue is automatically deposited into a joint UTMA account and that Nathan owns 100% of post-tax proceeds is therefore removed. For narrative continuity, payments first belong to the named seller/account holder under the applicable paid-app terms; Clifford and Heather can then make a separately documented family decision about savings for Nathan. The precise banking, tax, and beneficial-ownership arrangement remains an open legal/accounting detail, not an Apple rule.

### 1.3 Price and revenue split

The App Store's launch-era commercial model was commonly described as **70% to the developer and 30% to Apple**. Apple's 2008 announcement of the App Store developer model and later public filings describing the 2009 programme corroborate that split. [Sources C and D]

For a $0.99 listing, do not write that Nathan personally receives exactly $0.693 per download. The developer-side amount is subject to the applicable contract, settlement, refunds, taxes, and the identity of the contractual seller. In narrative dialogue, “Apple keeps 30%; the developer gets 70%” is a reasonable simplified explanation, not a complete accounting ledger.

---

## 2. iPhone 3GS hardware and iPhone OS 3.x memory

### 2.1 Hardware baseline

The following are suitable high-level constraints for scenes set in late 2009:

- **CPU:** Samsung S5PC100 / ARM Cortex-A8, reported at 600 MHz in the iPhone 3GS.
- **GPU:** PowerVR SGX graphics family (commonly identified as SGX535 in contemporary development references); Apple's June 2009 announcement explicitly confirms OpenGL ES 2.0 support.
- **RAM:** 256 MB physical memory in the iPhone 3GS. This is the total device memory, not memory reserved for one application.
- **Display:** 3.5-inch, 480 × 320 pixels, approximately 163 ppi.

The 600 MHz S5PC100 / 256 MB specifications are supported by a contemporaneous June 2009 teardown report and specialist hardware references rather than Apple's June 2009 press release. A September 2009 iPhone-game performance presentation also contains Instruments traces using the `IMGSGX535GLDriv` driver, which corroborates the SGX535 identification. Apple's own announcement confirms OpenGL ES 2.0. [Sources E, F, H, I]

**Colour depth:** The previous claim of an 18-bit display (262,144 colours) is removed from the canonical baseline. Third-party specification pages disagree about how to describe the panel's colour depth, and the primary Apple announcement does not settle that technical detail. It is not important to the story's current engineering constraints.

### 2.2 Memory is shared; do not invent a fixed per-app allowance

The device's 256 MB is shared by the operating system, system services, background processes, and the foreground application. The usable amount changes with the system state. It is not defensible to split it into a universal “120–130 MB for the system” and “125–135 MB for apps” partition, nor to present a single fixed app cap as a general iPhone OS 3.1 rule.

Apple's archived memory guidance says that iOS does not use disk-backed swap in the conventional desktop sense. When free pages fall below a system-computed threshold, iOS may send a low-memory notification; applications should release recreatable objects and caches. If memory pressure remains, the system may terminate applications. The documentation describes a computed threshold, **not** public numeric thresholds in megabytes. [Source G]

For application code, use the public-era UIKit mechanisms rather than presenting internal memory-watcher states as the app developer's API:

- `applicationDidReceiveMemoryWarning:`
- `didReceiveMemoryWarning`
- `UIApplicationDidReceiveMemoryWarningNotification`

The identifiers `OSMemoryNotificationLevelWarning` and `OSMemoryNotificationLevelUrgent`, and the previously stated 40–50 MB / 15–20 MB trigger values, are removed from the canonical narrative. They are not a defensible public contract for an iPhone OS 3.1 application. Do not make a character claim that an app is guaranteed to receive a warning at a particular free-RAM value before termination.

### 2.3 Nathan's 35 MB budget and the stress-test figures

A **35 MB working-set target** can remain as Nathan's own conservative engineering budget. It is a character's design target, not an Apple-imposed limit or a universal iPhone 3GS app ceiling.

The currently used figures — 200 agents, 60 FPS, 28.4 MB, and a temporary 45 MB spike — must be framed as **fictional measurements from Nathan's own build**, not published hardware specifications. To make them technically credible when drafted into the episode, state what was measured and under what conditions:

- exact device and iPhone OS version;
- debug or release build;
- test-scene contents, agent count, and duration;
- whether the figure means heap allocations, live allocations, or process resident/footprint memory;
- whether 60 FPS is sustained or an average, and how frame time was sampled.

Do not call “heap”, “resident memory”, “allocated bytes”, and “physical RAM used” interchangeable quantities.

**Object pooling:** A fixed-capacity pool can reduce repeated allocation/deallocation, allocator churn, and fragmentation risk. It does not magically reduce the bytes occupied by objects that remain live; preallocating a pool can itself increase the working set. In the story, pooling should solve an allocation-stability problem, while memory reduction should come from smaller data structures, fewer simultaneous assets, asset streaming, cache eviction, or a smaller pool.

The 45 MB spike should be an earlier failed stress-test result that motivates optimisation. If Nathan later claims to have met a sustained 35 MB budget, the post-optimisation test must demonstrate that result under a defined workload.

---

## 3. Source register and confidence

| ID | Source | What it supports | Confidence / limitation |
| :--- | :--- | :--- | :--- |
| A | [Apple Registered iPhone Developer Agreement, filed 24 March 2009 (Exhibit G)](https://docs.justia.com/cases/federal/district-courts/california/candce/5:2008cv03468/205349/146/7.html) | Adult account holder; explicit supervised parent/guardian permission for 13+ minors to share credentials; parent responsibility | Contemporaneous copy reproduced in a court filing; applies to the Registered iPhone Developer agreement, not by itself the full paid distribution contract |
| B | [iPhone Developer Program License Agreement, revision 17 March 2009 (archived copy)](https://www.eff.org/files/20100302_iphone_dev_agr.pdf) | Legal-age/authorized-organization signer; account holder responsibility; Apple selection/signing; separate Schedule 2 for paid apps | The PDF bears revision “3-17-09”; the linked copy does not include the separate Schedule 2 |
| C | [Apple, “Apple Announces iPhone 2.0 Software Beta”, 6 March 2008](https://www.apple.com/newsroom/2008/03/06Apple-Announces-iPhone-2-0-Software-Beta/) | Launch-era 70/30 developer/Apple revenue model | Historical launch policy; not a full statement of the later paid-app settlement process |
| D | [Appiphany Technologies Holdings, 2011 Form 10-K](https://www.sec.gov/Archives/edgar/data/1490054/000107878211002280/appiphany10k043011.htm) | A company reports entering the iPhone Developer Program in June 2009 and describes Apple’s 30% / developer’s 70% model | Contemporaneous company filing, but not Apple's own agreement |
| E | [iFixit iPhone Comparison — iPhone 3GS](https://www.ifixit.com/Wiki/iPhone_Comparison) | Display size/resolution/density, PowerVR SGX family, 600 MHz Cortex-A8, 256 MB RAM | Specialist secondary hardware reference; Apple did not publish every internal component in its launch release |
| F | [Apple, “Apple Announces the New iPhone 3GS”, 8 June 2009](https://www.apple.com/newsroom/2009/06/08Apple-Announces-the-New-iPhone-3GS-The-Fastest-Most-Powerful-iPhone-Yet/) | iPhone OS 3.0, OpenGL ES 2.0, launch-era features and capabilities | Primary Apple press release; not a full technical datasheet |
| G | [Apple Developer Archive — Memory Usage Performance Guidelines, “Tips for Allocating Memory”](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/ManagingMemory/Articles/MemoryAlloc.html) | No disk-backed swap; low-memory warnings, releasing references/caches, possible process termination | Apple archived developer guidance; current archive page is dated 2013, so it supports the general memory-management model, not a numeric 2009 threshold |
| H | [WIRED, “iPhone Teardown Reveals Underclocked 833MHz CPU”, 19 June 2009](https://www.wired.com/2009/06/iphone-teardown-reveals-underclocked-833mhz-cpu/) | Identifies the Samsung S5PC100 at 600 MHz and reports 256 MB memory | Contemporary teardown reporting; its explanation of why Apple chose 600 MHz is inference, not an Apple statement |
| I | [Noel Llopis, “Squeezing Every Drop Of Performance Out Of The iPhone”, iPhoneGames Summit, September 2009](https://gamesfromwithin.com/wp-content/uploads/2009/09/iPhone_performance.pdf) | Shows Instruments used for frame-rate, CPU, OpenGL ES and memory profiling on a real iPhone; includes the SGX535 driver identifier | Contemporary developer presentation; useful for realistic profiling practices, not a specification or benchmark of Nathan's fictional game |

### Open research questions

1. The exact 2009 version of Schedule 2 and its tax/payment workflow has not been recovered here. Do not write specific payout-bank, W-9, or minor-beneficiary rules until that schedule and applicable tax rules are checked.
2. The precise maximum memory footprint tolerated by a particular iPhone 3GS running iPhone OS 3.1 is not established by the cited public Apple guidance. Do not use a universal numeric termination threshold.
3. If an episode depends on Nathan's exact memory measurements, treat those values as results from a reproducible in-story benchmark, not as generic specifications of the 3GS.
