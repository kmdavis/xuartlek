---
title: Thelonésë Jobs
type: place
publish: false
draft: true
gm: kevan
aliases: ["Jobs"]
location: Thelonésë
tags: ["campaign/votgz", "gm/kevan"]
---

This file tracks available work in Thelonésë--both public postings and NPC-offered opportunities.

---

## The Job Board

The bulletin board at The Mariner's Rest posts public work opportunities. Torvald curates it loosely--he'll pull down anything obviously shady, but otherwise lets the market sort itself.

<job>
---
id: cargo-escort-mosshollow
category: escort
status: completed
offered-by: bren-kettleworth
difficulty: moderate
preconditions: []
unlocks: []
---

### Cargo Escort -- Moss Hollow Village

Guard a merchant wagon heading inland to Moss Hollow Village. Two days round trip, departing tomorrow at dawn.

**Accept**: Speak to Bren Kettleworth at the chandlery.

**Details**: A wagon carrying ship supplies and trade goods needs protection on the road to Moss Hollow. Standard jungle route--wildlife, occasional bandits, nothing unusual. Bren wants capable guards who won't slow the wagon down.

**Complications**:
- If the party encounters trouble on the trail, the merchant will remember their competence (or lack thereof)
- The route passes near logging camps--opportunity to deliver Rask's message en route

**Reward**:
- 50gp total for the round trip
- Bren's goodwill (useful for future ship supply discounts)
</job>

<job>
---
id: cargo-escort-westward
category: escort
status: available
offered-by: mira-saltwell
difficulty: moderate
preconditions: []
unlocks: []
---

### Cargo Escort -- Westward Bound

A merchant ship heading to the outer islands seeks capable guards for the voyage. Two weeks round trip, standard hazard rates.

**Accept**: Speak to Captain Voss at the *Silver Gull* (Dock 3). Mira can provide an introduction.

**Details**: The *Silver Gull* departs in three days, carrying trade goods to several outer island settlements. Captain wants visible security--pirates have been more active lately.

**Complications**:
- If the party investigates the cargo, they'll find it's legitimate but includes sealed crates the captain won't discuss
- If pirates do attack, they're after those specific crates

**Reward**:
- 50gp per person for the round trip
- Free passage and meals
</job>

<job>
---
id: missing-sailor
category: investigation
status: available
offered-by: torvald-greaves
difficulty: easy
preconditions: []
unlocks: []
---

### Missing Sailor

Crewman from the *Stormchaser* hasn't reported back. Ship leaves tomorrow. Captain offering coin for his return--or at least word of his fate.

**Accept**: Speak to Captain Hollis at the *Stormchaser* (Dock 7), or find Darik and send him back yourself.

**Details**: Darik Voss, human male, late twenties, missing for two days. Last seen heading toward the northeast quarter after shore leave started. His shipmates suspect he found trouble at The Spring Tide.

**Complications**:
- If the party asks at The Spring Tide, Yannick remembers him--he lost badly at cards and left in a foul mood
- If they search the northeast quarter, they'll find he got into a fight and is recovering at a dockside flophouse, too embarrassed to face his captain

**Reward**:
- 10gp for information leading to his return
- 5gp if he's confirmed dead (captain needs to know)
</job>

<job>
---
id: rat-problem
category: extermination
status: available
offered-by: orlan-thatch
difficulty: trivial
preconditions: []
unlocks: []
---

### Rat Problem at the Warehouse

Vermin infestation in Dock Street warehouse. Owner wants it handled before the next shipment arrives.

**Accept**: Find Harmon Creek at his warehouse on Dock Street (third building past the chandlery). Orlan can point the way.

**Details**: Standard pest control. The warehouse stores grain and dried goods--rats have gotten in through gaps in the foundation. Owner's too cheap to hire a proper exterminator.

**Complications**:
- If the party thoroughly investigates, they'll find the rats are unusually large--something in the grain is affecting them
- If they report this to Harmon, he pays extra to keep quiet (smuggled alchemical supplies)
- If they report to the constables, Harmon is fined and his warehouse searched; he blames the party publicly, and Orlan is annoyed they made trouble for a customer
- If they blackmail Harmon, he pays--but remembers, and he has friends

**Reward**:
- 5gp for clearing the rats
- 15gp bonus for discretion about the grain
</job>

---

## NPC Job Offerings

### Mira Saltwell -- Port Master

Mira occasionally needs tasks handled that fall outside official channels. She's discreet about who she asks.

<job>
---
id: manifest-discrepancy
category: investigation
status: available
offered-by: mira-saltwell
difficulty: moderate
preconditions: []
unlocks: [job:miras-bigger-problem]
---

### Manifest Discrepancy

A ship's cargo doesn't match its manifest. Mira needs someone to look into it quietly--before she decides whether to involve the constables.

**Details**: The *Bright Fortune* arrived yesterday with cargo listed as "textiles and pottery." The hold smells wrong--tar and metal, not cloth and clay. Captain claims everything's in order. Mira doesn't believe him.

**Complications**:
- If the party searches the hold, they'll find weapons hidden beneath the legitimate cargo
- If they confront the captain, he claims ignorance--says he was paid to deliver sealed crates, no questions asked
- If they trace the delivery, it leads to one of Lord Thassaril's stewards
- If they report to the constables immediately, Mira is irritated--she asked for discretion, not a formal investigation; she'll pay but won't offer future work
- If they tip off the captain, he dumps the cargo and sails; Mira never learns the truth and the party gets nothing

**Reward**:
- 30gp for a full report
- Mira owes them a favor (future information, expedited paperwork)
</job>

<job>
---
id: miras-bigger-problem
category: investigation
status: locked
offered-by: mira-saltwell
difficulty: hard
preconditions: [job:manifest-discrepancy]
unlocks: []
---

### The Steward's Cargo

Following up on the weapons shipment. Who's arming up on the island, and why?

**Details**: Lord Thassaril's steward ordered weapons delivered to the interior. That's not illegal--lords arm their guards--but the quantity suggests more than guard duty. Mira wants to know what's brewing before it becomes her problem.

**Complications**:
- If the party investigates openly, the steward claims the weapons are for a new logging camp's security
- If they investigate covertly, they'll discover the weapons are being stockpiled--the guild is preparing for potential conflict with the lords
- If they report to Mira, she's conflicted--she sympathizes with the workers but can't ignore armed insurrection
- If they report to the constables, Captain Ashward investigates formally; the guild knows they were betrayed by outsiders and becomes hostile; Rask considers them enemies
- If they report to the lords, the nobles move to disarm the guild preemptively; workers' conditions worsen; Rask and the guild remember who sold them out
- If they warn Rask, he's grateful but suspicious--how did they learn about the weapons? Trust must be earned before he'll explain the guild's position

**Reward**:
- 75gp for a complete picture
- Future warning if trouble's coming to port
</job>

---

### Korva Steelhand -- Weaponsmith

Korva doesn't chat, but she notices capable people. Those who've proven themselves might find her offering work.

<job>
---
id: korvas-debt-collection
category: retrieval
status: available
offered-by: korva-steelhand
difficulty: easy
preconditions: []
unlocks: [job:korvas-bigger-problem]
---

### Outstanding Payment

A customer took delivery on a commissioned blade but hasn't paid the balance. Korva wants her money--or her sword back.

**Details**: Varen Haelstrom, a minor merchant, commissioned a fine short sword three months ago. Paid half upfront, promised the rest on delivery. He's been dodging Korva ever since. She's not interested in constable involvement--too slow, too public.

**Complications**:
- If the party confronts Varen, he claims financial hardship--he can pay half now, the rest in a month
- If they investigate, they'll find he's actually flush with coin--he's just trying to welch
- If they threaten him, he folds immediately and pays in full with apologies

**Reward**:
- 15gp (her markup on recovering her own money)
- 10% discount on Korva's work going forward
</job>

<job>
---
id: korvas-bigger-problem
category: retrieval
status: locked
offered-by: korva-steelhand
difficulty: moderate
preconditions: [job:korvas-debt-collection]
unlocks: []
---

### The Stolen Shipment

A crate of raw steel--her best supplier's work--went missing from the docks. Korva needs it back before she falls behind on commissions.

**Details**: The shipment arrived three days ago but never made it to her shop. Port records show it was signed for, but the signature isn't hers. Someone's either stealing from the docks or specifically targeting her.

**Complications**:
- If the party checks port records, the forged signature is sloppy--someone who knew her name but not her hand
- If they ask around the docks, a loader remembers a woman matching Korva's description (sort of) claiming the crate
- If they find the thief, it's a rival smith from Sielmoro trying to sabotage her business

**Reward**:
- 40gp plus the party's pick of her ready stock (common weapons/armor)
- A custom commission at cost (materials only)
</job>

---

### Torvald Greaves -- Tavernkeeper

Torvald hears everything. Sometimes he passes along opportunities to people he likes.

<job>
---
id: discrete-delivery
category: courier
status: available
offered-by: torvald-greaves
completed-by: the merchant's mistress (east side townhouse)
difficulty: easy
preconditions: []
unlocks: []
---

### Discrete Delivery

A guest needs a package delivered across town. Nothing illegal--just private.

**Details**: A merchant staying at the inn needs medicine delivered to his mistress on the east side of town. His wife is also staying at the inn. He'll pay well for discretion.

**Complications**:
- If the party delivers without incident, straightforward payment
- If they're spotted by the wife's maid (who frequents the bazaar), they'll need to explain themselves or improvise
- If they blackmail the merchant, Torvald will hear about it and they're no longer welcome

**Reward**:
- 5gp for successful delivery
- Torvald's good opinion (worth more than coin in a port town)
</job>

---

### Yannick Corwen -- The Spring Tide

Yannick always has angles. He'll offer work to interesting newcomers--nothing too dangerous, just enough to see what they're made of.

<job>
---
id: spring-tide-invitation
category: social
status: available
offered-by: yannick-corwen
difficulty: trivial
preconditions: []
unlocks: [job:yannicks-favor]
---

### An Invitation

Yannick invites the party to join the card tables--membership waived for one evening. A chance to make connections and demonstrate their... talents.

**Details**: Not really a job--more an audition. Yannick wants to see how they handle themselves among the town's better class of scoundrel. Win or lose at cards, it's how they play that matters.

**Complications**:
- If they cheat and get caught, they're out--but Yannick notes their boldness
- If they cheat and don't get caught, Yannick notices anyway--and approves
- If they play straight and lose gracefully, they've made friends
- If they're rude to other guests, doors close

**Reward**:
- A night of entertainment
- Access to The Spring Tide's social network
</job>

<job>
---
id: yannicks-favor
category: social
status: locked
offered-by: yannick-corwen
difficulty: moderate
preconditions: [job:spring-tide-invitation]
unlocks: []
---

### A Small Favor

Yannick has a delicate matter. A member owes significant gambling debts and is making noise about exposure. Yannick would like the situation... resolved.

**Details**: Lord Thassaril's steward has been losing badly for months. Now he's threatening to tell the constables that The Spring Tide runs illegal games unless his debts are forgiven. Yannick needs someone to convince him that's a poor idea.

**Complications**:
- If the party threatens the steward, he backs down but holds a grudge
- If they investigate his finances, they'll find he's been embezzling from Lord Thassaril to cover his losses
- If they bring this to Yannick, he'll use it as leverage instead--cleaner than violence
- If they report any of this to the constables, they've made an enemy of Yannick

**Reward**:
- 50gp for a quiet resolution
- Yannick owes them a favor (information, introductions, a blind eye)
</job>

---

### Rask Embertooth -- Guild Representative

Rask speaks for the workers. He's careful about who he trusts, but outsiders sometimes prove useful--no local entanglements.

<job>
---
id: guild-message
category: courier
status: completed
offered-by: rask-embertooth
completed-by: Camp One foreman (nearest logging camp)
difficulty: easy
preconditions: []
unlocks: [job:guild-investigation]
---

### Message to the Interior

Rask needs a message delivered to the logging camps. Simple courier work--if you don't mind a day's hike through jungle.

**Details**: Official guild correspondence to the camp foremen. Nothing sensitive, just scheduling and wage information. Rask's usual runners are busy, and he doesn't trust the lords' messengers.

**Complications**:
- If the party delivers without incident, straightforward
- If they read the message, it's genuinely mundane--but Rask will know they broke the seal
- If they encounter trouble on the trail (wildlife, bandits), the foremen will be grateful for warning

**Reward**:
- 10gp for delivery
- Guild goodwill (helpful if they need workers' cooperation later)
</job>

<job>
---
id: guild-investigation
category: investigation
status: active
offered-by: rask-embertooth
difficulty: hard
preconditions: [job:guild-message]
unlocks: []
---

### The Disappeared Workers

Three workers have vanished from Camp Six over the past month. The lords say they deserted. Rask doesn't believe it.

**Details**: Experienced loggers don't just walk away from wages owed. Something's happening at Camp Six, and Lord Maevathar's overseers aren't talking. Rask needs outsiders to find the truth--locals asking questions would raise suspicion.

**Complications**:
- If the party investigates the camp, the overseer is evasive but not hostile
- If they search the surrounding jungle, they'll find signs of large predator activity--something's hunting near the camp
- If they confront Lord Maevathar (or his representatives), he claims ignorance and offers compensation to the families--too quickly, too smoothly
- If they dig deeper, they'll discover the lord knew about the predator and didn't warn the workers because evacuation would delay timber shipments
- If they report to the constables, Captain Ashward has no jurisdiction over the lords' estates; he can only suggest the families pursue civil remedies--which they can't afford
- If they go public (tavern gossip, town crier), Lord Maevathar's reputation suffers and he becomes a dangerous enemy; the guild is grateful but the party has made a powerful foe
- If they kill the predator themselves, the immediate threat ends but the lord's negligence goes unpunished; Rask appreciates the help but wants justice, not just safety

**Reward**:
- 75gp for finding the truth
- Guild support in future endeavors (500+ workers across the island)
</job>

---

### Vellum Ashworth -- Harbor Surgeon

Vellum doesn't offer jobs often. When he does, it's because he needs something he can't handle alone.

<job>
---
id: medical-supplies
category: retrieval
status: available
offered-by: vellum-ashworth
completed-by: vellum-ashworth
difficulty: easy
preconditions: []
unlocks: []
---

### Medical Supply Run

A ship carrying medical supplies is delayed. Vellum needs specific herbs from the interior before his stocks run out.

**Details**: The logged trails lead to villages that cultivate medicinal plants. A day's round trip for someone who knows the path--or two days for someone figuring it out. Vellum will provide a list and directions.

**Complications**:
- If the party haggles with the villagers, they'll get a worse price--these aren't merchants
- If they're respectful and pay fairly, the village herbalist might share knowledge or offer to supply Vellum directly
- If they mention Vellum, the herbalist's demeanor changes--she knows him, not fondly

**Reward**:
- 15gp for the supplies
- Free medical care for a month
</job>

---

## NPC Referrals

Some NPCs don't offer work directly but can point the party toward opportunities.

### Orlan Thatch -- General Merchant
Doesn't have jobs, but knows who needs help. "Talk to Bren about that cargo problem" or "Korva was looking for capable sorts." A useful first contact who'll steer newcomers right.

### Bren Kettleworth -- Ship Chandler
Similarly connected but more focused--she'll mention captains looking for crew, ships needing repairs, or cargo opportunities. Practical, maritime-focused referrals.

### Isindrel Maevathar -- Noble Daughter
Won't offer work (she's never worked a day in her life), but she gossips freely. Mentions what she's heard about the lords' troubles, the guild's complaints, interesting strangers in port. Information, not employment.

### Aejylinn Olythos -- Noble Daughter
Even less likely to offer work. But if she takes a liking to someone, she might mention something useful--obliquely, carefully, deniably.

---

## NPC Declines

### Caelvorn Ashward -- Constable Captain
Doesn't freelance. If he needs help, it goes through official channels--temporary deputization, posted bounties, formal requests. He won't ask strangers to handle constabulary business off the books.

### Elara Thornwood -- Circuit Judge
Absolutely not. The judge maintains strict propriety. She neither offers nor accepts informal assistance. Everything through proper legal channels.

---

## Job Status Key

- **available**: Can be taken now
- **locked**: Requires completing preconditions
- **active**: Currently in progress
- **completed**: Finished
- **failed**: Failed or abandoned
- **expired**: No longer available
