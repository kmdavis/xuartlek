---
hp: "30"
ac: "18"
modifier: "7"
level: "2"
player: Ellen
class: Ranger
ancestry: Catfolk
source: Foundry export fvtt-Actor-espera-(ellen)-hwYBWPzvf14UmP1C.json
---

```statblock
layout: Basic Pathfinder 2e Layout
name: Espera
level: 2
ancestry: Catfolk # unrendered
heritage: Sharp-Eared Catfolk # unrendered
background: Bounty Hunter # unrendered
class: Ranger # unrendered

rare_03: Ranger # class
rare_04: Bounty Hunter # background
size: Medium
trait_01: Catfolk
trait_02: Humanoid

modifier: 7 # unrendered
perception:
  - name: Perception
    desc: "Perception +7"
languages:
- Amurrun
- Common
skills:
  acrobatics: +7
  athletics: +5
  deception: +6
  diplomacy: +6
  medicine: +5
  nature: +5
  stealth: +7
  survival: +5
  legal_lore: +5
abilityMods: [1,3,1,1,1,2]

ac: 18 # unrendered
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +7; __Ref__: +9; __Will__: +5"
hp: 30 # unrendered
health:
  - name: "HP"
    desc: 30
saves: # unrendered
  fortitude: +7
  reflex: +9
  will: +5

speed: 25 feet
attacks:
  - name: "Melee"
    desc: "⬻ dagger +7 (Agile, Finesse, Thrown 10, Versatile S) __Damage__ 1d4+1 piercing"
  - name: "Ranged"
    desc: "⬻ crossbow +7 __Range__ 120 ft.; __Reload__ 1; __Damage__ 1d8 piercing"
```

## Feats and Features

### Class Features

**Hunt Prey** *Level 1*

`ranger`

When you focus your attention on a single foe, you become unstoppable in your pursuit. You gain the Hunt Prey action.

**Hunter's Edge** *Level 1*

`ranger`

You have trained to become a skilled hunter and tracker, gaining an extra benefit when you Hunt Prey depending on the focus of your training. Choose a hunter's edge.

- Flurry

- Outwit

- Precision

**Outwit** *Level 1*

`ranger`

You are talented at outwitting your prey. You gain a +1 circumstance bonus to AC against your prey's attacks and a +2 circumstance bonus to Deception checks, Intimidation checks, Stealth checks, and any checks to Recall Knowledge about the prey.

### Class Feats

**Animal Companion (Ranger)** *Level 1*

`ranger`

You gain the service of a young animal companion that travels with you and obeys simple commands. When you Hunt Prey, your animal companion gains the action's benefits and your hunter's edge benefit if you have one.

- Effect: Hunter's Edge, Flurry

- Effect: Hunter's Edge, Outwit

- Effect: Hunter's Edge, Precision

**Crossbow Ace** *Level 1*

`ranger`

**Requirements** You are wielding a crossbow with reload 1 or higher.

Your deep understanding of the crossbow allows you to reload efficiently while moving yourself out of the line of return fire. Either Create a Diversion or Take Cover, then Interact to reload. As normal, you must meet the requirements to Take Cover; you must be Prone, benefiting from cover, or near a feature that allows you to Take Cover.

**Pirate Dedication** *Level 2*

`archetype`  `dedication`

As a pirate, you sail the seas in search of enemy ships to plunder and great adventures to embark on. You gain the Additional Lore general feat for Sailing Lore or for a specific coastal city you have a connection to (such as Port Peril Lore). You ignore the effects of difficult terrain or uneven ground caused by unstable ground (such as the deck of a ship). Additionally, you gain the Boarding Assault action.

Pirate

### Ancestry Features

**Land on Your Feet** *Level 1*

`catfolk`

When you fall, you take only half the normal damage and don't land Prone.

### Ancestry Feats

**Cat's Luck** *Level 1*

`catfolk`  `fortune`

**Frequency** once per day

**Trigger** You fail a Reflex saving throw.

You instinctively twist away from danger. You can reroll the triggering saving throw and use the better result.

### Skill Feats

**Experienced Smuggler** *Level 1*

`general`  `skill`

You often smuggle things past the authorities. When the GM rolls your Stealth check to see if a passive observer notices a small item you've Concealed, the GM uses the number rolled or 10—whichever is higher—as the result of your die roll, adding it to your Stealth modifier to determine your Stealth check result. If you're a master in Stealth, the GM uses the number rolled or 15, and if you're legendary in Stealth, you automatically succeed at hiding a small concealed item from passive observers. This provides no benefits when a creature attempts a Perception check while actively searching you for Hidden items.

**PFS Note** This feat allows you to Earn Income with Underworld Lore with tasks of your level -1 (instead of the normal level -2).

**Experienced Tracker** *Level 1*

`general`  `skill`

Tracking is second nature to you, and when necessary you can follow a trail without pause. You can Track while moving at full Speed by taking a –5 penalty to your Survival check. If you're a master in Survival, you don't take the –5 penalty. If you're legendary in Survival, you no longer need to roll a new Survival check every hour when tracking, though you still need to roll whenever there are significant changes in the trail.


## Inventory

### Currency

| Denomination | Qty |
|---|---|
| Silver (sp) | 81 |
| **Total** | **8.10 gp** |

### Held

| Item | Qty | Bulk | Price |
|---|---|---|---|
| Crossbow |  | 1 | 3 gp |
| Dagger |  | 0.1 | 2 sp |

### Carried

| Item | Qty | Bulk | Price |
|---|---|---|---|
| Backpack |  |  | 1 sp |
| Bedroll |  | 0.1 | 2 cp |
| Bolts | 4 | 0.1 | 1 sp |
| Chalk | 10 |  | 1 cp |
| Fanged |  |  | 30 gp |
| Flint and Steel |  |  | 5 cp |
| Leather Armor |  | 1 | 2 gp |
| Rations | 2 | 0.1 | 4 sp |
| Rope |  | 0.1 | 5 sp |
| Soap |  |  | 2 cp |
| Torch | 5 | 0.1 | 1 cp |
| Waterskin |  | 0.1 | 5 cp |

## Companion: Drak

*Snake familiar. Uses Espera's AC, saving throws and Perception,
and has 5 Hit Points per level. These values are derived from
Espera's sheet; a familiar stores none of its own.*

```statblock
layout: Basic Pathfinder 2e Layout
name: Drak
level: 2

rare_03: Familiar # class
rare_04: Espera's companion # background
size: Tiny
trait_01: Snake
trait_02: Minion

modifier: 7 # unrendered
perception:
  - name: Perception
    desc: "Perception +7"
abilityMods: [0,0,0,0,0,0]

ac: 18 # unrendered
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +7; __Ref__: +9; __Will__: +5"
hp: 10 # unrendered
health:
  - name: "HP"
    desc: 10

speed: 25 feet
```
