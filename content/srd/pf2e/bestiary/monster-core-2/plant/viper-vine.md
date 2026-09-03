---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Viper Vine"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/large
statblock: inline
name: "Viper Vine"
level: 13
source: "Monster Core 2"
aon_id: "creature-4612"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4612"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Viper Vine"
level: "Creature 13"
size: "Large"
trait_01: "Plant"
modifier: 22
perception:
  - name: "Perception"
    desc: "Perception +22; low-light vision, tremorsense (imprecise) 60 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +27, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +24"
abilityMods: [8, 5, 7, -4, 5, -3]
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +26; __Ref__: +24; __Will__: +22"
hp: 270
health:
  - name: "HP"
    desc: "270; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]] 15"
abilities_mid:
  - name: "Cold Vulnerability"
    desc: "When exposed to a cold effect, the viper vine is overwhelmed by lethargy, becoming [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed]] 1 for 1d4 rounds."
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +27 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 3d6+11 piercing plus 3d6 poison"
  - name: "Melee"
    desc: "⬻ vine +25 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 3d10+11 bludgeoning plus Grab"
abilities_bot:
  - name: "Captivating Pollen"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/incapacitation|Incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]]) The viper vine releases a 60-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Emanation|emanation]] of invisible pollen that stays in the air for 5 rounds unless dispersed by a moderate or stronger wind. Each creature that enters or starts its turn in the area must succeed at a DC 33 Will save or be captivated. The viper vine can't use Captivating Pollen for 1d4 rounds."
  - name: "Critical Success"
    desc: "The creature is unaffected and is temporarily immune to Captivating Pollen for 24 hours."
  - name: "Success"
    desc: "The creature is [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened]] 1."
  - name: "Failure"
    desc: "The creature is [[srd/pf2e/compendium/rules-elements/conditions#Fascinated|fascinated]], and it must spend each of its actions to move closer to the viper vine as expediently as possible while avoiding obvious dangers. If a captivated creature is adjacent to the viper vine, it stays still and doesn't act. It ceases to be fascinated if it's no longer in the pollen aura at the end of its turn."
  - name: "Critical Failure"
    desc: "As failure, plus the creature is [[srd/pf2e/compendium/rules-elements/conditions#Stupefied|stupefied]] 2 for 24 hours."
  - name: "Constrict"
    desc: "⬻ 3d8+8 bludgeoning, DC 33 Viper Vine Pollen While viper vine pollen degrades quickly after it’s harvested carefully from the plant, a character who has a set of alchemical tools can gather and preserve 1d6 doses of pollen with a successful DC 33 [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] or [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] check and 10 minutes of work. A single dose of viper vine pollen is worth 300 gp as raw materials for crafting any alchemical or magical item that creates an [[srd/pf2e/compendium/rules-elements/traits/player-core/incapacitation|incapacitation]] effect."
sourcebook: "_Monster Core 2_, page 350."
```

```encounter-table
name: Viper Vine
creatures:
  - 1: Viper Vine
```
