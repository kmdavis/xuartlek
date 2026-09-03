---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ayngavhaul"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/devil
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Ayngavhaul"
level: 13
source: "Monster Core 2"
aon_id: "creature-4329"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4329"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Ayngavhaul"
level: "Creature 13"
size: "Medium"
trait_01: "Devil"
trait_02: "Fiend"
trait_03: "Unholy"
modifier: 26
perception:
  - name: "Perception"
    desc: "Perception +26; greater darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/languages#Empyrean|Empyrean]]; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +27, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +26, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +24, [[srd/pf2e/compendium/rules-elements/skills/lore|Library Lore]] +27, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +24"
abilityMods: [4, 4, 5, 8, 5, 5]
abilities_top:
  - name: "Personal Library"
    desc: "Any tomes an ayngavhaul is reading or referencing for their current work can be stored in the devil's personal library, a floating collecting of tomes revolving around the devil that can be used offensively or defensively. Retrieving or returning a tome requires an Interact action."
ac: 34
armorclass:
  - name: "AC"
    desc: "34; __Fort__: +23; __Ref__: +20; __Will__: +26 +1 status to all saves vs. magic"
hp: 240
health:
  - name: "HP"
    desc: "240; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]]; __Resistances__ physical 10 (except [[srd/pf2e/compendium/equipment/materials/silver-object-high-grade|silver]]); __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|holy]] 10"
abilities_mid:
  - name: "Spellblock Tome"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|manipulate]])"
  - name: "Trigger"
    desc: "The ayngavhaul is targeted by a spell"
  - name: "Effect"
    desc: "The ayngavhaul flings a tome from its personal library at the spell. The devil must attempt a DC 5 flat check. On a success, the tome fully absorbs the effects of the spell and burns up into a harmless pile of ash. Regardless of the result, the devil can't use this ability again for 1d4 rounds."
speed: "15 feet, fly 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +25 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]]) __Damage__ 3d8+8 slashing"
  - name: "Ranged"
    desc: "⬻ searing words +27 ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]], range 60 feet, [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]]) __Damage__ 3d10+8 mental plus 1d6 fire and poison minds"
abilities_bot:
  - name: "Herald Heresy"
    desc: "⬽ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]]) The ayngavhaul imparts blasphemous thoughts into the minds of all non-devil creatures within a 20-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Burst|burst]] up to 60 feet away. An affected creature takes 2d10 mental damage plus 2d10 spirit damage and must attempt a DC 33 Will save. Affected creatures gain a cumulative +1 circumstance bonus (up to a total of +4) to saves against all future attempts to Herald Heresy for 1 minute, as they become inured to the blasphemies."
  - name: "Critical Success"
    desc: "The creature is unaffected and becomes temporarily immune for 1 hour."
  - name: "Success"
    desc: "The creature takes half damage."
  - name: "Failure"
    desc: "The creature takes full damage and becomes [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed]] 1."
  - name: "Critical Failure"
    desc: "The creature takes double damage and becomes slowed 2."
  - name: "Poison Minds"
    desc: "Creatures hit by the ayngavhaul's searing words must succeed at a DC 33 Will saving throw or become [[srd/pf2e/compendium/rules-elements/conditions#Stupefied|stupefied]] 1 for 1 round (or stupefied 2 on a critical failure). If the target is trained in [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]], they take a –2 circumstance penalty to their save. Beyond Peer Review Each ayngavhaul carries a personal tome that is an ever-changing encyclopedia of knowledge and literature laced with malevolent bias and half-truths. When an ayngavhaul reads their personal tome, they can intrinsically understand the concepts presented and the true nature of the text, which is often needed to add credibility to their arguments. Depending on the personality of the ayngavhaul, they will sometimes take on a tome they find as their new personal tome, transfixed by the new truths found within. The tome is illegible to all other creatures."
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 33, attack +25 - __Cantrips (6th)__ [[srd/pf2e/compendium/spells/cantrips/daze|Daze]], [[srd/pf2e/compendium/spells/cantrips/detect-magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/figment|Figment]], [[srd/pf2e/compendium/spells/cantrips/phase-bolt|Phase Bolt]], [[srd/pf2e/compendium/spells/cantrips/telekinetic-hand|Telekinetic Hand]] - __5th__ [[srd/pf2e/compendium/spells/rank-5/banishment|Banishment]], [[srd/pf2e/compendium/spells/rank-5/mind-probe|Mind Probe]], [[srd/pf2e/compendium/spells/rank-5/subconscious-suggestion|Subconscious Suggestion]] - __6th__ [[srd/pf2e/compendium/spells/rank-6/dominate|Dominate]], [[srd/pf2e/compendium/spells/rank-6/never-mind|Never Mind]]"
sourcebook: "_Monster Core 2_, page 101."
```

```encounter-table
name: Ayngavhaul
creatures:
  - 1: Ayngavhaul
```
