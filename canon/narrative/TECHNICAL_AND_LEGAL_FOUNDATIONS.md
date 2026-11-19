# Real-World Technical and Legal Baseline (2009)

Status: RESEARCHED REAL-WORLD BASELINE — CLAIMS QUALIFIED BY SOURCE  
Updated: 2026-11-19

This document establishes the researched real-world 2009 baseline for technology and law in the parallel-world setting. It does not define the full fictional universe: explicit divergences in canon/narrative/WORLD_DIFFERENCE_REGISTRY.md override this baseline for the story. In the absence of a registered divergence, do not assume the parallel world differs from the real-world baseline. This document also separates (1) facts supported by sources from (2) fictional engineering choices and (3) unresolved legal/accounting details. A source from 2010 or later is not silently treated as the exact contract or implementation that applied on a particular day in 2009.

---

## 1. Apple Developer account, minor participation and App Store sales

### 1.1 What the 2009-era documents support

A copy of Apple's **Registered iPhone Developer Agreement**, revised 20 October 2008 and filed as an exhibit in a US court on 24 March 2009, says the registered developer must be of legal age of majority. It also contains a specific exception: a parent or legal guardian may allow a person aged 13 up to the age of majority to share the adult's Apple ID and password **solely under that adult's supervision**. The parent/guardian remains responsible for that person's compliance.

This is strong period evidence for Nathan, aged 13, being able to participate in development under Clifford's supervision. It does **not** make Nathan the independent account holder, nor does it by itself prove that every action under the separate paid-app distribution contract may be delegated to him.

A separate iPhone Developer Program License Agreement dated 2 March 2010 (near-period evidence, but not an exact copy of the agreement in force on 18 November 2009) requires the contracting person to be of legal age, or to have authority to bind the company/organization on whose behalf they sign. It also says a paid application requires a separate agreement with Apple (Schedule 2). The public copy of that program agreement is not the complete Paid Applications Agreement.

**Canon rule:** Clifford is the adult account holder and publisher. Nathan writes the code and prepares the build under Clifford's supervision. Clifford reviews/accepts the contractual terms and performs the final account-holder submission to iTunes Connect. Do not describe Nathan as independently holding the paid developer account.

### 1.2 Use the right program name

Apple's 6 March 2008 announcement says the **Standard iPhone Developer Program** included the ability to distribute applications through the App Store and cost US$99 per year at launch. It separately described the **Enterprise Program**, priced at US$299. A contemporaneous Apple developer-session transcript describes Enterprise distribution as internal-only, for people within the developer's own organization.

Therefore, a game intended for public sale in the App Store must not be described as using an "individual/enterprise account" or as being published through the Enterprise Program. For this story, use **Clifford's Standard iPhone Developer Program account**. The exact historical membership price at the moment of the story should not be asserted without a dated price source.

### 1.3 Revenue, tax and custodial savings

Apple announced the App Store's standard launch split in 2008: developers retained 70% of sales revenue and Apple retained 30%. The US$0.99 price in the story is therefore compatible with the historic model, before any separate tax/accounting consequences.

The current canon's claim that Apple deposits sales revenue directly into a joint UTMA account "co-signed" by Clifford and Heather is **not established by the cited Apple agreements**. App Store contracting, seller/payee identity, tax forms, bank details, copyright ownership and the later transfer of money to a minor are separate issues.

California Probate Code §3910 states that only one person may be custodian for a minor's custodial property. If the story retains a California UTMA account, it must not call Clifford and Heather joint co-custodians under that provision. More importantly, do not imply that a UTMA account automatically receives App Store proceeds or that Nathan automatically owns all net revenue. The legal and tax route by which money earned through Clifford's developer account becomes Nathan's property remains a **family/legal arrangement**, not an Apple feature. Keep the precise arrangement unspecified until it is deliberately researched and chosen.

The W-9 assertion in the former version is also too strong: the public period sources reviewed here do not establish that submitting a W-9 was a clause of the Registered iPhone Developer Agreement or a universal requirement attached to every developer account. Tax documentation may be required by the paid-app/payment setup, but the exact 2009 forms and payee should be sourced separately before being stated as fact.

---

## 2. iPhone 3GS hardware baseline

The iPhone 3GS was announced on 8 June 2009 and shipped with iPhone OS 3.0. A teardown published by iFixit on 19 June 2009 identifies a Samsung **256 MB DDR SDRAM** memory component. This supports the 256 MB physical-RAM figure; it does not tell us how much memory a particular app could safely use at runtime.

| Component | Supported period detail |
|---|---|
| SoC / CPU | Samsung S5PC100, ARM Cortex-A8, 600 MHz in the iPhone 3GS |
| GPU | PowerVR SGX family; use SGX535 only where the hardware source for the exact chip revision is retained |
| Display | 3.5-inch, 480 × 320 pixels, 163 ppi |
| Physical RAM | 256 MB DDR SDRAM |
| OS at launch | iPhone OS 3.0; the story's November 2009 test device may be described as running iPhone OS 3.1 if that version is explicitly established in its timeline |

**Correction:** do not call the memory "256 MB Mobile DDR" unless a source for that exact memory type is supplied. The contemporary teardown labels the Samsung component DDR SDRAM. The former claim that the 3GS display is 18-bit/262,144 colours is also not retained: the available device specification sources do not support that figure consistently, and the story does not need colour depth.

---

## 3. Memory behaviour: what the operating system did, and what it did not promise

iPhone OS did not provide a fixed public "40 MB per-app limit" for every iPhone 3GS application. Low-memory warnings depended on **system-wide memory pressure** and reclaimable memory. Apple documentation describes warnings delivered to the running application and possible process termination if pressure persists; it does not define universal 40 MB, 50 MB, 100 MB or 120 MB thresholds for the iPhone 3GS.

Use the public UIKit memory-warning concepts, such as `applicationDidReceiveMemoryWarning:` and `UIApplicationDidReceiveMemoryWarningNotification`, rather than the unsupported names `OSMemoryNotificationLevelWarning` and `OSMemoryNotificationLevelUrgent`. Do not turn a particular app's observed footprint into a universal OS kill threshold.

### 3.1 Nathan's 35 MB target

The **below-35 MB target is an in-universe engineering budget**, not an Apple-imposed ceiling. It is a conservative target chosen by Nathan to leave headroom on a device with 256 MB total physical RAM and to reduce the risk of memory pressure across different usage conditions.

Be precise about the measurement:
- "Live heap allocations below 35 MB" describes Nathan's allocation measurement.
- It is not the same as total process resident memory, the device's free memory, or an operating-system limit.
- A test run reaching 45 MB is a measured result for this fictional build and workload, not proof that iPhone OS would terminate it.

### 3.2 Object pooling

The story's benchmark of 200 concurrent agents, 60 FPS, 18% CPU and 28.4 MB on 15 October is an **in-universe result** recorded in EVT-013. The later 28.4-to-45 MB stress run with uncompressed audio is likewise a fictional profiler observation, not a published iPhone 3GS benchmark.

A preallocated object pool is technically plausible: it can reduce repeated `new`/`delete` traffic, allocation churn and unpredictable allocator work during gameplay. It does not automatically prove that all heap fragmentation disappears or that peak memory falls; the pool itself reserves memory and must be sized correctly. Describe it as a bounded-allocation strategy, not a magical fix.

### 3.3 Background audio and push notifications

In the iPhone SDK era before iOS 4 multitasking, Apple's built-in iPod app could continue playing while a third-party app was in the foreground, but ordinary third-party apps could not freely continue their own execution after being backgrounded. This makes "the user listens to iPod music while playing" a plausible user scenario; it does not establish a numerical memory threshold.

Push notifications should not be described as background work that necessarily competes with the game for a large app-memory allocation. They are an external notification mechanism, not evidence for a 40 MB/50 MB kill threshold.

---

## 4. App Store review timing in November–December 2009

The statement in the earlier version that the November 2009 "average approval time" was **seven to fourteen business days** is unsupported and should not be repeated as a measured average.

A contemporaneous developer question dated 1 December 2009 reports that the App Store was then displaying an estimate that 95% of submitted applications were reviewed within 14 days, referring to 20 November. This is secondary evidence quoting the estimate, not a guarantee and not proof that the 14 days were business days. The story's 18 November submission and 3 December release are 15 calendar days apart, so the timeline is plausible as a fictional case slightly beyond that reported estimate.

There is a source-date conflict around the exact status label **"Waiting for Review"**: MacRumors reported that label on 12 November 2009, while Apple's developer news page dated 8 December 2009 calls it a newly added status. The label can remain in the 20 November scene because a contemporaneous report predates the scene, but the research record must preserve the conflicting release dates rather than claim certainty.

---

## 5. Sources and confidence

1. [Apple Registered iPhone Developer Agreement, Rev. 10/20/08 — filed 24 March 2009 (PDF exhibit)](https://cases.justia.com/federal/district-courts/california/candce/5%3A2008cv03468/205349/146/7.pdf) — **high confidence for the quoted 2008 registered-developer terms**; it is not the paid-app distribution agreement.
2. [iPhone Developer Program License Agreement, 2 March 2010 (PDF, Electronic Frontier Foundation)](https://www.eff.org/files/20100302_iphone_dev_agr.pdf) — **high confidence for the text of that 2010 agreement; medium confidence as a proxy for November 2009**. It requires legal age/authority and refers paid apps to a separate Schedule 2.
3. [Apple, iPhone 2.0 Software Beta announcement, 6 March 2008](https://www.apple.com/newsroom/2008/03/06Apple-Announces-iPhone-2-0-Software-Beta/) — **high confidence** for Standard Program App Store distribution and the 70/30 launch revenue split.
4. [Apple iPhone Developer Enterprise Program technical talk (2008)](https://nonstrict.eu/wwdcindex/tech-talks/2008-13/) — **contemporaneous technical-session transcript** describing Enterprise distribution as internal to an organization.
5. [iFixit, iPhone 3GS teardown, 19 June 2009](https://www.ifixit.com/News/14161/iphone-3g-s-teardown) and [teardown guide component list](https://ifixit-guide-pdfs.s3.amazonaws.com/pdf/ifixit/guide_817_en.pdf) — **high confidence for the photographed/identified 256 MB DDR SDRAM component**.
6. [Apple, iPhone 3GS announcement, 8 June 2009](https://www.apple.com/newsroom/2009/06/08Apple-Announces-the-New-iPhone-3GS-The-Fastest-Most-Powerful-iPhone-Yet/) — **high confidence** for announcement date and launch OS 3.0.
7. [Apple archived memory-allocation guidance](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/ManagingMemory/Articles/MemoryAlloc.html) — **high confidence for Apple's described memory-warning behaviour**, but the archived page is later than iPhone OS 3.1 and is not evidence for exact 2009 thresholds.
8. [Daring Fireball, "One App at a Time", 14 March 2008](https://daringfireball.net/2008/03/one_app_at_a_time) — **contemporaneous secondary explanation** of the pre-iOS-4 foreground-only restriction for ordinary third-party apps and built-in iPod background playback.
9. [MacRumors, App Store status updates, 12 November 2009](https://www.macrumors.com/2009/11/12/apple-adds-status-updates-to-app-store-approval-process/) and [Apple Developer News, 8 December 2009](https://developer.apple.com/news/?id=11132009a) — **conflicting publication dates** for the "Waiting for Review" status.
10. [Contemporaneous developer discussion, 1 December 2009](https://stackoverflow.com/questions/1823424/does-apples-iphone-app-review-process-use-a-business-or-calendar-day/1823452) — **secondary evidence only** for the reported 95%-within-14-days estimate.
11. [California Probate Code §3910](https://law.justia.com/codes/california/code-prob/division-4/part-9/section-3910/) — **current statutory text** states one custodian per minor custodianship; do not treat this page alone as a complete legal opinion about Nathan's earnings.

---

## 6. Open canon decisions

- Confirm whether Clifford's account is a personal Standard Program membership or belongs to a named legal company. Do not combine the labels "individual" and "enterprise".
- Decide who is the legal seller/payee and how money is transferred to Nathan. Do not state that the UTMA account receives App Store payments automatically.
- If retaining a California UTMA account, identify one custodian and separately establish the legal/tax route for transferring the proceeds.
- Obtain the exact 2009 Paid Applications Agreement / Schedule 2 before adding specific claims about W-9s, banking details, payment timing or indemnification.
- Keep the 35 MB target as Nathan's own budget. Never present it as an iPhone 3GS operating-system limit.
