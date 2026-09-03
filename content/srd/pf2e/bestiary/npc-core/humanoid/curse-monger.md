---
obsidianUIMode: preview
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
aon_id: "creature-3544"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3544"
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
    desc: "Perception +23"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Aklo|Aklo]], [[srd/pf2e/compendium/rules-elements/languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/languages#Common|Common]], Daemonic, [[srd/pf2e/compendium/rules-elements/languages#Fey|Fey]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +25, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +25, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +23, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +29, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +24"
abilityMods: [1, 5, 3, 8, 4, 4]
abilities_top:
  - name: "Incurable Curse"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/curse|curse]]) The curse monger is permanently [[srd/pf2e/compendium/rules-elements/conditions#Clumsy|clumsy 1]], [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained 1]], [[srd/pf2e/compendium/rules-elements/conditions#Enfeebled|enfeebled 1]], or [[srd/pf2e/compendium/rules-elements/conditions#Stupefied|stupefied 1]] by a curse that can't be removed from them in any way. The GM chooses the condition and decides whether the curse is [[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]], or [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]]."
  - name: "Items"
    desc: "_+1 [[srd/pf2e/compendium/equipment/runes/resilient-major|resilient]] [[srd/pf2e/compendium/equipment/armor#Explorer's Clothing|explorer's clothing]]_, _+1 [[srd/pf2e/compendium/equipment/runes/striking-major|striking]] [[srd/pf2e/compendium/equipment/runes/wounding|wounding]] [[srd/pf2e/compendium/equipment/weapons/knife/sickle|sickle]]_, [[srd/pf2e/compendium/spells/rank-4/fly|_scroll of fly_]]"
ac: 35
armorclass:
  - name: "AC"
    desc: "35; __Fort__: +23; __Ref__: +25; __Will__: +26 –2 to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/curse|curses]]"
hp: 230
health:
  - name: "HP"
    desc: "230"
abilities_mid:
  - name: "Cursed Aura"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/curse|curse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]]) 30 feet. The very earth and air around the curse monger are poisoned by the curses that burden their soul. Any creature who enters or starts their turn in the aura must succeed at a DC 31 Will save or be [[srd/pf2e/compendium/rules-elements/conditions#Doomed|doomed 1]] (or doomed 2 on a critical failure). Regardless of the result of its save, the creature is then temporarily immune for 1 hour."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _sickle_ +25 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/trip|Trip]]) __Damage__ 2d4+13 slashing plus 1d6 persistent bleed"
  - name: "Melee"
    desc: "⬻ fist +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+13 bludgeoning"
abilities_bot:
  - name: "Share Burden"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/curse|Curse]]) The curse monger shares their awful burden with one creature they can see within 120 feet. The target must succeed at a DC 37 Will save or be afflicted with the same condition as the curse monger's incurable curse for 24 hours. On a critical failure, the curse's value is 2. The curse lasts for 24 hours but can be removed (unlike the incurable curse), and ends if the curse monger dies. This action has the same tradition trait as incurable curse. Jinxed Curse Mongers For certain curse mongers, spreading the curse is an involuntary part of the curse itself. When a jinxed curse monger starts their turn, Share Burden automatically attempts to curse a random creature in range that's not already cursed; this doesn't require an action. If the attempt fails, the curse monger must spend their first actions on that turn casting a [[srd/pf2e/compendium/rules-elements/traits/player-core/curse|curse]] spell ([[srd/pf2e/compendium/spells/rank-6/cursed-metamorphosis|_cursed metamorphosis_]], [[srd/pf2e/compendium/spells/rank-6/never-mind|_never mind_]], [[srd/pf2e/compendium/spells/rank-6/spellwrack|_spellwrack_]], [[srd/pf2e/compendium/spells/rank-5/mariners-curse|_mariner's curse_]], [[srd/pf2e/compendium/spells/rank-4/outcasts-curse|_outcast's curse_]], or [[srd/pf2e/compendium/spells/rank-1/ill-omen|_ill omen_]]). If the curse monger doesn't want to curse anyone, the GM determines a target at random. The target doesn't have to be an enemy but can't be the curse monger."
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 37, attack +29 - __Cantrips (7th)__ [[srd/pf2e/compendium/spells/cantrips/daze|Daze]], [[srd/pf2e/compendium/spells/cantrips/figment|Figment]], [[srd/pf2e/compendium/spells/cantrips/telekinetic-hand|Telekinetic Hand]], [[srd/pf2e/compendium/spells/cantrips/message|Message]], [[srd/pf2e/compendium/spells/cantrips/void-warp|Void Warp]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/bane|Bane]], [[srd/pf2e/compendium/spells/rank-1/fear|Fear]], [[srd/pf2e/compendium/spells/rank-1/ill-omen|Ill Omen]] (3 slots) - __2nd__ [[srd/pf2e/compendium/spells/rank-2/darkness|Darkness]], [[srd/pf2e/compendium/spells/rank-2/laughing-fit|Laughing Fit]], [[srd/pf2e/compendium/spells/rank-2/paranoia|Paranoia]] (3 slots) - __3rd__ [[srd/pf2e/compendium/spells/rank-3/hypercognition|Hypercognition]], [[srd/pf2e/compendium/spells/rank-3/slow|Slow]], [[srd/pf2e/compendium/spells/rank-3/mind-reading|Mind Reading]] (3 slots) - __4th__ [[srd/pf2e/compendium/spells/rank-2/blood-vendetta|Blood Vendetta]], [[srd/pf2e/compendium/spells/rank-4/outcasts-curse|Outcast's Curse]], [[srd/pf2e/compendium/spells/rank-4/vision-of-death|Vision of Death]] (3 slots) - __5th__ [[srd/pf2e/compendium/spells/rank-5/false-vision|False Vision]], [[srd/pf2e/compendium/spells/rank-5/mariners-curse|Mariner's Curse]], [[srd/pf2e/compendium/spells/rank-5/wave-of-despair|Wave of Despair]] (3 slots) - __6th__ [[srd/pf2e/compendium/spells/rank-6/never-mind|Never Mind]], [[srd/pf2e/compendium/spells/rank-6/phantasmal-calamity|Phantasmal Calamity]], [[srd/pf2e/compendium/spells/rank-6/spellwrack|Spellwrack]] (3 slots) - __7th__ [[srd/pf2e/compendium/spells/rank-6/cursed-metamorphosis|Cursed Metamorphosis]], [[srd/pf2e/compendium/spells/rank-6/dominate|Dominate]], [[srd/pf2e/compendium/spells/rank-7/possession|Possession]] (3 slots)"
sourcebook: "_NPC Core_, page 104."
```

```encounter-table
name: Curse Monger
creatures:
  - 1: Curse Monger
```
