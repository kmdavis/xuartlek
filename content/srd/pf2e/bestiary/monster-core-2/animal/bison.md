---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Bison"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/animal
  - pf2e/creature/trait/large
statblock: inline
name: "Bison"
level: 4
source: "Monster Core 2"
aon_id: "creature-4283"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4283"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Bison"
level: "Creature 4"
size: "Large"
trait_01: "Animal"
modifier: 8
perception:
  - name: "Perception"
    desc: "Perception +8; scent (imprecise) 60 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +12, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +10"
abilityMods: [6, 3, 5, -5, 2, -1]
ac: 20
armorclass:
  - name: "AC"
    desc: "20; __Fort__: +13; __Ref__: +11; __Will__: +8"
hp: 70
health:
  - name: "HP"
    desc: "70"
abilities_mid:
  - name: "Cold Adaptation"
    desc: "The bison reduces the effects it suffers from [[srd/pf2e/books/gm-core/chapter-2-building-games/environment#Temperature|cold environments]] by one step."
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ hoof +14 __Damage__ 2d6+6 bludgeoning"
  - name: "Melee"
    desc: "⬻ horn +12 __Damage__ 2d8+6 piercing plus Knockdown"
abilities_bot:
  - name: "Pointed Charge"
    desc: "⬺ The bison surges forward at its foe, horns lowered. It [[srd/pf2e/compendium/rules-elements/actions/player-core#Stride|Strides]] twice. If the bison ends its movement within melee range of an enemy, it makes a horn Strike against that enemy. This Strike gains the [[srd/pf2e/compendium/rules-elements/traits/player-core/fatal|fatal d12]] trait."
  - name: "Rolling Thunder"
    desc: "⬽ The bison kicks up dust and shakes the ground as it charges. The stampeding bison [[srd/pf2e/compendium/rules-elements/actions/player-core#Stride|Strides]] up to twice its Speed in a straight [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Line|line]] and can move through the spaces of Medium or smaller creatures. Each creature whose space it moves through takes 4d6+6 bludgeoning damage (DC 21 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save). Multiple bison can participate in Rolling Thunder by spending this ability's actions and waiting to charge until the herd is ready. Before the beginning of their next turn, they can then charge as a reaction triggered by an adjacent bison beginning its Rolling Thunder charge. All bison in the combined charge must charge in parallel lines, so the areas can't overlap. The combined charge deals an additional 3d6 bludgeoning damage to creatures in the area, and a creature that fails the Reflex saving throw is also knocked [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]]. Bison Drives Hunting bison is a communal endeavor. [[srd/pf2e/compendium/gm/creature-families/centaur|Centaurs]] from the plains organize into hunting brigades and run alongside members of a stampeding herd, lancing and shooting them from close range. Less mobile peoples use disguises to shepherd bison into position before scaring them to rush over sheer drops or into corrals where they can be slaughtered. A single bison herd can provide enough meat, hides, and furs for an entire community."
sourcebook: "_Monster Core 2_, page 59."
```

```encounter-table
name: Bison
creatures:
  - 1: Bison
```
