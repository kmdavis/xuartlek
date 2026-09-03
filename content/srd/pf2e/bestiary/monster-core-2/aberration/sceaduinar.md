---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Sceaduinar"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/void
  - pf2e/creature/trait/medium
  - pf2e/creature/trait/negative
statblock: inline
name: "Sceaduinar"
level: 7
source: "Monster Core 2"
aon_id: "creature-4540"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4540"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Sceaduinar"
level: "Creature 7"
size: "Medium"
trait_01: "Aberration"
trait_02: "Rare"
trait_03: "Void"
trait_04: "Negative"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; greater darkvision, lifesense 120 feet"
languages: "Aklo"
skills:
  - name: "Skills"
    desc: "Acrobatics +17, Athletics +13, Intimidation +13, Occultism +15, Stealth +17"
abilityMods: [2, 6, 4, 2, 4, 0]
ac: 25
armorclass:
  - name: "AC"
    desc: "25; __Fort__: +16; __Ref__: +18; __Will__: +14 +1 status to all saves vs. magic"
hp: 100
health:
  - name: "HP"
    desc: "100 (void healing (page 363)); __Immunities__ death effects, drained; __Weaknesses__ vitality 10, Resistances physical 5 (except adamantine)"
abilities_mid:
  - name: "Void Child"
    desc: "Sceaduinar have neither souls nor the ability to create. A sceaduinar is immune to effects that target a soul (such as _seize soul_ or a _resurrect_ ritual) or that require knowledge of a creature's identity (such as _scrying_), and critically fails Crafting checks."
speed: "30 feet, fly 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +18 (Agile, finesse, magical) __Damage__ 2d6+4 piercing plus 2d6 void and drain life"
  - name: "Melee"
    desc: "⬻ wing +18 (Agile, finesse, magical, reach 10 feet) __Damage__ 2d6+4 slashing plus 2d6 void"
abilities_bot:
  - name: "Drain Life"
    desc: "(Occult) When the sceaduinar damages a living creature with its jaws Strike, the sceaduinar gains 5 temporary Hit Points and the creature must succeed at a DC 25 Fortitude save or become drained 1. Further damage dealt to the creature by the sceaduinar increases the drained value by 1 on a failed save, to a maximum of drained 4."
  - name: "Entropic Touch"
    desc: "Void damage dealt by a sceaduinar damages undead and creatures with void healing as if it were vitality damage. The sceaduinar's melee Strikes have the benefits of the _ghost touch_ property rune on attacks against incorporeal undead. Sceaduinar Crystals Sceaduinar congregate on the great crystalline knots of void energy that accrete in the Void. Sceaduinar prod treelike crystal growths to produce dangerous items akin to miniaturized black holes or great structures that echo with eerie chimes. Sceaduinar also stimulate these aggregations of crystals to yield other sceaduinar and similar hateful creatures of unlife."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 25 - __Cantrips (4th)__ Void Warp - __2nd__ Silence - __3rd__ Grim Tendrils, Harm (×3) - __4th__ Darkness, Dispel Magic, Harm, Translocate"
sourcebook: "_Monster Core 2_, page 281."
```

```encounter-table
name: Sceaduinar
creatures:
  - 1: Sceaduinar
```
