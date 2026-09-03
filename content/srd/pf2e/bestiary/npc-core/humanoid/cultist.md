---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Cultist"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Cultist"
level: 1
source: "NPC Core"
aon_id: "creature-3534"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3534"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Cultist"
level: "Creature 1"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 4
perception:
  - name: "Perception"
    desc: "Perception +4"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/lore|Lore]] +8, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +3, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +3, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +4, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +4, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +6"
abilityMods: [4, 3, 2, 1, -1, 0]
abilities_top:
  - name: "Items"
    desc: "cultist garb (functions as [[srd/pf2e/compendium/equipment/armor#Leather Armor|leather armor]]), Dagger, occult text"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +7; __Ref__: +8; __Will__: +4 (or +2 vs. higher-ranking members of the cult)"
hp: 20
health:
  - name: "HP"
    desc: "20"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+4 piercing"
  - name: "Melee"
    desc: "⬻ fist +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+4 bludgeoning"
  - name: "Ranged"
    desc: "⬻ dagger +6 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+4 piercing"
abilities_bot:
  - name: "Fanatical Frenzy"
    desc: "⬻"
  - name: "Requirements"
    desc: "The cultist has taken damage and is neither [[srd/pf2e/compendium/rules-elements/conditions#Fatigued|fatigued]] nor already in a frenzy"
  - name: "Effect"
    desc: "The cultist flies into a frenzy that lasts 1 minute. While frenzied, the cultist gains a +1 status bonus to attack rolls and a +2 status bonus to damage rolls, and they take a –2 penalty to AC. The cultist can't voluntarily stop their frenzy. After their frenzy, the cultist is fatigued."
sourcebook: "_NPC Core_, page 97."
```

```encounter-table
name: Cultist
creatures:
  - 1: Cultist
```
