# Technical and Legal Foundations (2009 Period-Accuracy)

Status: AUTHORITATIVE CANONICAL REFERENCE  
Updated: 2026-11-19

---

## 1. Apple Developer Program: Legal & Contractual Framework (2009)

### Legal Age of Majority & Account Ownership
In March 2009 (and throughout iOS 3.x), the **Apple iPhone Developer Program License Agreement** strictly required that the registered account holder be of legal age of majority (18 years old or older in the United States) to execute the contract, agree to indemnification clauses, and submit W-9 tax identification information.

* **Account Holder:** **Clifford Callahan**. Clifford holds a paid individual/enterprise Apple Developer Account registered to his executive corporate profile.
* **Supervised Minor Participation:** In accordance with Apple's developer guidelines, minors aged 13 and older are permitted to develop software, test builds on provisioned test devices, and author code under the direct supervision and legal sponsorship of a parent or legal guardian.
* **Banking & Custodial Earnings:** 
  - Revenue generated from App Store sales ($0.99 per download, with Apple retaining the standard 30% commission) is deposited directly into a designated custodial bank account (Uniform Transfers to Minors Act — UTMA) co-signed by Clifford and Heather Callahan.
  - Nathan retains 100% of net proceeds after taxes for his independent savings and hardware purchases, managed with parental oversight.
* **Attribution:** The binary is published under Clifford's developer portal, with the internal product credits, design, and code authored entirely by Nathan Callahan.

---

## 2. iPhone 3GS Hardware Specifications & Memory Architecture

### Hardware Baseline (June 2009 Launch Specifications)
* **Processor (SoC):** Samsung S5PC100 (ARM Cortex-A8 core, underclocked to 600 MHz from 833 MHz for battery/thermal stabilization).
* **Graphics Processor (GPU):** Imagination Technologies PowerVR SGX535 (OpenGL ES 1.1 and 2.0 capable, hardware transform & lighting).
* **Display:** 3.5-inch diagonal TFT LCD, 480 × 320 pixels at 163 ppi (HVGA), 18-bit color (262,144 colors).
* **Total Physical Memory (RAM):** **256 MB Mobile DDR**. (Double the 128 MB found in the original iPhone and iPhone 3G).

### Memory Partitioning under iPhone OS 3.1
The total 256 MB RAM is divided between system software and userland applications:
1. **System & Kernel Overhead (~120–130 MB):** 
   - Kernel, SpringBoard, CoreServices, audio daemons, telemetry, telephony baseband buffers, and shared graphics memory.
2. **Available User Space (~125–135 MB):** 
   - The total remaining physical RAM available for foreground applications under clean boot conditions.
3. **Low-Memory Warning & Termination Triggers:**
   - **Level 1 Warning (`OSMemoryNotificationLevelWarning`):** Dispatched to the active app when system-wide available RAM falls below ~40–50 MB (meaning the foreground app is consuming ~65–80 MB).
   - **Level 2 / Termination (`OSMemoryNotificationLevelUrgent` / `SIGKILL`):** The system watchdog forcibly terminates the active app without crash dumps if total allocations push system free RAM below ~15–20 MB (app footprint exceeding ~100–120 MB).

### Reconciling the 35–40 MB Engineering Budget
In Episode 4 (`EP04`), Nathan targets an active heap footprint **below 35 MB**. 
* **Reasoning:** This is not because 40 MB represents a hard hardware ceiling, but because a professional mobile game in 2009 must leave ample headroom for the user to listen to background iPod music, receive incoming push notifications, or handle transient memory spikes during texture streaming without triggering the OS memory warning threshold.
* **Stress Test Benchmark (EP02/EP04):** During extreme stress testing with 200 concurrent pathfinding agents and full uncompressed audio buffers, memory spikes from 28.4 MB to 45 MB, demonstrating the necessity of Nathan's **static object pooling** in C++ to prevent heap fragmentation.
