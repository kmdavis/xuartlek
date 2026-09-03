---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Myceloid"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/fungus
  - pf2e/creature/trait/medium
statblock: inline
name: "Myceloid"
level: 4
source: "Monster Core 2"
aon_id: "creature-4485"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4485"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Myceloid"
level: "Creature 4"
size: "Medium"
trait_01: "Fungus"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; darkvision, scent (imprecise) 30 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Sakvroth|Sakvroth]]; telepathy 100 feet (myceloids and those afflicted by purple pox only)"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +11, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +10"
abilityMods: [4, 3, 4, -1, 2, 0]
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +14; __Ref__: +9; __Will__: +10"
hp: 70
health:
  - name: "HP"
    desc: "70; __Weaknesses__ slashing 5"
abilities_mid:
  - name: "Spore Pop"
    desc: "If a myceloid is reduced to 0 HP by a critical hit, they pop, forcing them to immediately Emit Spores, even if they've already used the ability that day."
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +14 __Damage__ 2d6+4 bludgeoning plus purple pox"
abilities_bot:
  - name: "Emit Spores"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The myceloid expels spores in a 10-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Burst|burst]] centered on a corner of their own space. This cloud lasts until the start of the myceloid's next turn. Each creature that's in the cloud or enters it is exposed to purple pox."
  - name: "Purple Pox"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/disease|Disease]]) Myceloids are immune"
  - name: "Saving Throw"
    desc: "DC 20 Fortitude"
  - name: "Onset"
    desc: "1 minute"
  - name: "Stage 1"
    desc: "2d6 poison damage and [[srd/pf2e/compendium/rules-elements/conditions#Stupefied|stupefied]] 1 (1 day)"
  - name: "Stage 2"
    desc: "6d6 poison damage, stupefied 3, and the creature is compelled to seek out the nearest myceloid colony—this compulsion is a [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]] and [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|emotion]] effect (1 day)"
  - name: "Stage 3"
    desc: "The creature dies. After 24 hours, its corpse becomes bloated and bursts, releasing a new, fully grown myceloid."
  - name: "Spore Domination"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|Emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/incapacitation|incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]]) The myceloid targets one creature affected by purple pox within 60 feet. That creature must attempt a DC 22 Will save. It's then temporarily immune to Spore Domination for 10 minutes."
  - name: "Critical Success"
    desc: "The target is unaffected."
  - name: "Success"
    desc: "Until the end of its next turn, the target is [[srd/pf2e/compendium/rules-elements/conditions#Helpful|helpful]] to myceloids and can't take [[srd/pf2e/books/player-core/chapter-7-spells/hostile-actions|hostile actions]] against them."
  - name: "Failure"
    desc: "As success, but for 1 minute."
  - name: "Critical Failure"
    desc: "As success, but until the purple pox is cured. Table Manners Myceloids eat communal meals consisting of a series of corpses, beginning with creatures they killed in combat, followed by any that died in service while controlled by Spore Domination. As they dine, they offer tasting notes, claiming they can taste intangibles like innocence or despair. They save any creature that died from purple pox as dessert. The new myceloid birthed from the corpse gets the first slice!"
sourcebook: "_Monster Core 2_, page 231."
```

```encounter-table
name: Myceloid
creatures:
  - 1: Myceloid
```
