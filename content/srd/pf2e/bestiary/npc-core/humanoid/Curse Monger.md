---
noteType: pf2eMonster
aliases: "Curse Monger"
tags:
  - pf2e/creature/level/14
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/medium
statblock: inline
name: "Curse Monger"
level: 14
source: "NPC Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3544"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Curse Monger"
level: "Creature 14"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Rare"
modifier: 23
perception:
  - name: "Perception"
    desc: "+23"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Aklo|Aklo]], [[srd/pf2e/compendium/rules-elements/Languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], Daemonic, [[srd/pf2e/compendium/rules-elements/Languages#Fey|Fey]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Arcana|Arcana]] +25, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +25, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +23, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +29, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +24"
abilityMods: [1, 5, 3, 8, 4, 4]
abilities_top:
  - name: "Incurable Curse"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Curse|curse]]) The curse monger is permanently [[srd/pf2e/compendium/rules-elements/Conditions#Clumsy|clumsy 1]], [[srd/pf2e/compendium/rules-elements/Conditions#Drained|drained 1]], [[srd/pf2e/compendium/rules-elements/Conditions#Enfeebled|enfeebled 1]], or [[srd/pf2e/compendium/rules-elements/Conditions#Stupefied|stupefied 1]] by a curse that can't be removed from them in any way. The GM chooses the condition and decides whether the curse is [[srd/pf2e/compendium/rules-elements/traits/player-core/Arcane|arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|occult]], or [[srd/pf2e/compendium/rules-elements/traits/player-core/Primal|primal]]."
  - name: "Items"
    desc: "_+1 [[srd/pf2e/compendium/equipment/runes/Resilient|resilient]] [[srd/pf2e/compendium/equipment/Armor#Explorer's Clothing|explorer's clothing]]_, _+1 [[srd/pf2e/compendium/equipment/runes/Striking|striking]] [[srd/pf2e/compendium/equipment/runes/Wounding|wounding]] [[srd/pf2e/compendium/equipment/weapons/knife/Sickle|sickle]]_, [[srd/pf2e/compendium/spells/rank-4/Fly|_scroll of fly_]]"
ac: 35
armorclass:
  - name: "AC"
    desc: "35; __Fort__: +23; __Ref__: +25; __Will__: +26 –2 to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Curse|curses]]"
hp: 230
health:
  - name: "HP"
    desc: "230"
abilities_mid:
  - name: "Cursed Aura"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Curse|curse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|occult]]) 30 feet. The very earth and air around the curse monger are poisoned by the curses that burden their soul. Any creature who enters or starts their turn in the aura must succeed at a DC 31 Will save or be [[srd/pf2e/compendium/rules-elements/Conditions#Doomed|doomed 1]] (or doomed 2 on a critical failure). Regardless of the result of its save, the creature is then temporarily immune for 1 hour."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _sickle_ +25 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Trip|Trip]]) __Damage__ 2d4+13 slashing plus 1d6 persistent bleed"
  - name: "Melee"
    desc: "⬻ fist +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|Unarmed]]) __Damage__ 1d4+13 bludgeoning"
abilities_bot:
  - name: "Share Burden"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Curse|Curse]]) The curse monger shares their awful burden with one creature they can see within 120 feet. The target must succeed at a DC 37 Will save or be afflicted with the same condition as the curse monger's incurable curse for 24 hours. On a critical failure, the curse's value is 2. The curse lasts for 24 hours but can be removed (unlike the incurable curse), and ends if the curse monger dies. This action has the same tradition trait as incurable curse. Jinxed Curse Mongers For certain curse mongers, spreading the curse is an involuntary part of the curse itself. When a jinxed curse monger starts their turn, Share Burden automatically attempts to curse a random creature in range that's not already cursed; this doesn't require an action. If the attempt fails, the curse monger must spend their first actions on that turn casting a [[srd/pf2e/compendium/rules-elements/traits/player-core/Curse|curse]] spell ([[srd/pf2e/compendium/spells/rank-6/Cursed Metamorphosis|_cursed metamorphosis_]], [[srd/pf2e/compendium/spells/rank-6/Never Mind|_never mind_]], [[srd/pf2e/compendium/spells/rank-6/Spellwrack|_spellwrack_]], [[srd/pf2e/compendium/spells/rank-5/Mariner's Curse|_mariner's curse_]], [[srd/pf2e/compendium/spells/rank-4/Outcast's Curse|_outcast's curse_]], or [[srd/pf2e/compendium/spells/rank-1/Ill Omen|_ill omen_]]). If the curse monger doesn't want to curse anyone, the GM determines a target at random. The target doesn't have to be an enemy but can't be the curse monger."
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 37, attack +29 - __Cantrips (7th)__ [[srd/pf2e/compendium/spells/cantrips/Daze|Daze]], [[srd/pf2e/compendium/spells/cantrips/Figment|Figment]], [[srd/pf2e/compendium/spells/cantrips/Telekinetic Hand|Telekinetic Hand]], [[srd/pf2e/compendium/spells/cantrips/Message|Message]], [[srd/pf2e/compendium/spells/cantrips/Void Warp|Void Warp]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Bane|Bane]], [[srd/pf2e/compendium/spells/rank-1/Fear|Fear]], [[srd/pf2e/compendium/spells/rank-1/Ill Omen|Ill Omen]] (3 slots) - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Darkness|Darkness]], [[srd/pf2e/compendium/spells/rank-2/Laughing Fit|Laughing Fit]], [[srd/pf2e/compendium/spells/rank-2/Paranoia|Paranoia]] (3 slots) - __3rd__ [[srd/pf2e/compendium/spells/rank-3/Hypercognition|Hypercognition]], [[srd/pf2e/compendium/spells/rank-3/Slow|Slow]], [[srd/pf2e/compendium/spells/rank-3/Mind Reading|Mind Reading]] (3 slots) - __4th__ [[srd/pf2e/compendium/spells/rank-2/Blood Vendetta|Blood Vendetta]], [[srd/pf2e/compendium/spells/rank-4/Outcast's Curse|Outcast's Curse]], [[srd/pf2e/compendium/spells/rank-4/Vision of Death|Vision of Death]] (3 slots) - __5th__ [[srd/pf2e/compendium/spells/rank-5/False Vision|False Vision]], [[srd/pf2e/compendium/spells/rank-5/Mariner's Curse|Mariner's Curse]], [[srd/pf2e/compendium/spells/rank-5/Wave of Despair|Wave of Despair]] (3 slots) - __6th__ [[srd/pf2e/compendium/spells/rank-6/Never Mind|Never Mind]], [[srd/pf2e/compendium/spells/rank-6/Phantasmal Calamity|Phantasmal Calamity]], [[srd/pf2e/compendium/spells/rank-6/Spellwrack|Spellwrack]] (3 slots) - __7th__ [[srd/pf2e/compendium/spells/rank-6/Cursed Metamorphosis|Cursed Metamorphosis]], [[srd/pf2e/compendium/spells/rank-6/Dominate|Dominate]], [[srd/pf2e/compendium/spells/rank-7/Possession|Possession]] (3 slots)"
sourcebook: "_NPC Core_, page 104."
```

```encounter-table
name: Curse Monger
creatures:
  - 1: Curse Monger
```
