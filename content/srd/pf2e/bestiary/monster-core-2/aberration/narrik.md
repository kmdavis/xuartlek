---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Narrik"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/large
statblock: inline
name: "Narrik"
level: 7
source: "Monster Core 2"
aon_id: "creature-4487"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4487"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Narrik"
level: "Creature 7"
size: "Large"
trait_01: "Aberration"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; darkvision, scent (imprecise) 120 feet, taste fear, vestigial eyes"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Aklo|Aklo]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +17, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +17, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +15, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +15"
abilityMods: [6, 4, 2, -1, 4, 2]
abilities_top:
  - name: "Taste Fear"
    desc: "A narrik viscerally tastes fear. They can use scent as a precise sense when detecting [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened]] creatures."
  - name: "Vestigial Eyes"
    desc: "A narrik's vision is limited. It's only a precise sense within 30 feet, and an imprecise sense beyond that."
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +18; __Ref__: +15; __Will__: +12"
hp: 130
health:
  - name: "HP"
    desc: "130; __Immunities__ precision"
abilities_mid:
  - name: "Quick Congeal"
    desc: "A narrik's strange body chemistry causes their blood to congeal almost instantly. They automatically succeeds at flat checks to recover from [[srd/pf2e/compendium/rules-elements/conditions#Persistent Damage|persistent bleed damage]]."
  - name: "Catalyzing Demise"
    desc: "⭓"
  - name: "Trigger"
    desc: "The narrik is reduced to 0 Hit Points"
  - name: "Effect"
    desc: "When a narrik is slain, their internal chemistry undergoes a violent chain reaction. They explode, and all creatures in a 5-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Emanation|emanation]] must succeed at a DC 25 Reflex save or be [[srd/pf2e/compendium/rules-elements/conditions#Immobilized|immobilized]] by tanglespit and exposed to psychotropic saliva."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +18 __Damage__ 2d6+8 piercing plus psychotropic saliva"
  - name: "Melee"
    desc: "⬻ claws +18 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]]) __Damage__ 2d4+8 slashing"
  - name: "Ranged"
    desc: "⬻ spit +16 (range increment 30 feet) __Damage__ tanglespit plus psychotropic saliva"
abilities_bot:
  - name: "Psychotropic Saliva"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]]) The target's [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened]] value doesn't automatically decrease at the end of its turn while affected by this poison"
  - name: "Saving Throw"
    desc: "DC 22 Fortitude; Maximum Duration 6 rounds"
  - name: "Stage 1"
    desc: "1d6 poison damage and frightened 1 (1 round)"
  - name: "Stage 2"
    desc: "1d8 poison damage and frightened 2 (1 round)"
  - name: "Stage 3"
    desc: "1d10 poison damage and frightened 3 (1 round)"
  - name: "Tanglespit"
    desc: "A creature hit by the narrik's tanglespit is [[srd/pf2e/compendium/rules-elements/conditions#Immobilized|immobilized]] as the viscous glob quickly solidifies. The DC to [[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escape]] or [[srd/pf2e/compendium/rules-elements/actions/player-core#Force Open|Force Open]] the tanglespit is 25. The glob becomes fragile and brittle after 1 minute, automatically freeing the creature. Alchemical Furnaces Most intelligent creatures avoid narriks, but some particularly brave— or foolhardy—deros and adventurers hunt them to harvest psychotropic saliva, tangle spit, and other alchemical additives. Because narriks' bodies explode upon death, hunters must capture living subjects to garner such materials."
sourcebook: "_Monster Core 2_, page 233."
```

```encounter-table
name: Narrik
creatures:
  - 1: Narrik
```
