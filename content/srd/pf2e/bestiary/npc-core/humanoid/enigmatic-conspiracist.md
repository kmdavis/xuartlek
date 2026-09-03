---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Enigmatic Conspiracist"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Enigmatic Conspiracist"
level: 4
source: "NPC Core"
aon_id: "creature-3536"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3536"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Enigmatic Conspiracist"
level: "Creature 4"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; (12 to [[srd/pf2e/compendium/rules-elements/actions/player-core#Sense Motive|Sense Motive]])"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Aklo|Aklo]], [[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Elven|Elven]], [[srd/pf2e/compendium/rules-elements/languages#Sakvroth|Sakvroth]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +12, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +9, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +11, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +12, [[srd/pf2e/compendium/rules-elements/skills/lore|Secret Society Lore]] +14, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +12, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +10"
abilityMods: [0, 4, 0, 2, 2, 3]
abilities_top:
  - name: "Items"
    desc: "_[[srd/pf2e/compendium/equipment/held-items/everlight-crystal|everlight crystal]]_, Leather Armor, Rapier, Shortbow (20 arrows)"
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +8; __Ref__: +12; __Will__: +12"
hp: 60
health:
  - name: "HP"
    desc: "60; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]] 5"
abilities_mid:
  - name: "Knowing Glance"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|visual]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]])"
  - name: "Trigger"
    desc: "The enigmatic conspiracist is targeted by a melee Strike or touch spell"
  - name: "Effect"
    desc: "With an uncanny look, the enigmatic conspiracist [[srd/pf2e/compendium/rules-elements/actions/player-core#Demoralize|Demoralizes]] the creature that targeted them. Demoralize loses the [[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|auditory]] trait and gains the [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|visual]] trait, and the conspiracist doesn't take a penalty if the creature doesn't understand their language. If the [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] check critically succeeds, the conspiracist [[srd/pf2e/books/player-core/chapter-8-playing-the-game/actions#Disrupting Actions|disrupts]] the triggering action."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ rapier +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d8]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disarm|Disarm]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 1d8+6 piercing plus spill secrets"
  - name: "Melee"
    desc: "⬻ fist +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+6 bludgeoning"
  - name: "Ranged"
    desc: "⬻ shortbow +14 ([[srd/pf2e/compendium/rules-elements/traits/player-core/deadly|deadly d10]], range increment 60 feet, reload 0) __Damage__ 1d6+6 piercing plus spill secrets"
abilities_bot:
  - name: "Spill Secrets"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|Occult]]) When the conspiracist critically hits with a Strike, the target must succeed at a DC 21 Will save or the enigmatic conspiracist perceives the target's surface thoughts for 1 round, as [[srd/pf2e/compendium/spells/rank-3/mind-reading|_mind reading_]]. This grants the conspiracist a +1 circumstance bonus to AC and saving throws against any creature whose mind they're reading."
  - name: "Unbelievable Connection"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|Occult]]) The enigmatic conspiracist recites a convoluted conspiracy theory about a creature within 30 feet, then attempts an [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] check against the Will DC of that creature. On a success, the target is [[srd/pf2e/compendium/rules-elements/conditions#Stupefied|stupefied 1]] for 1 minute and [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] against the conspiracist's attacks until no longer stupefied. Mystic Organizations Golarion has numerous secretive societies. The"
  - name: "Church of Razmir"
    desc: "offers a plan of 31 steps to divinity. The"
  - name: "Esoteric Order of the Palatine Eye"
    desc: "seeks celestial truths said to be granted by an ancient angel. The"
  - name: "Knights of the Aeon Star"
    desc: "search for secret lore. Followers of"
  - name: "Rivethun"
    desc: "dwarven animism, reach out to spirits to gain knowledge and earn favors."
sourcebook: "_NPC Core_, page 98."
```

```encounter-table
name: Enigmatic Conspiracist
creatures:
  - 1: Enigmatic Conspiracist
```
