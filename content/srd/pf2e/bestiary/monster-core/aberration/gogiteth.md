---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Gogiteth"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/large
statblock: inline
name: "Gogiteth"
level: 12
source: "Monster Core"
aon_id: "creature-3029"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3029"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Gogiteth"
level: "Creature 12"
size: "Large"
trait_01: "Aberration"
modifier: 21
perception:
  - name: "Perception"
    desc: "Perception +21; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Sakvroth|Sakvroth]]; (can't speak)"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +19, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +24, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +21, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +17"
abilityMods: [6, 3, 4, -2, 1, 0]
ac: 31
armorclass:
  - name: "AC"
    desc: "31; __Fort__: +25; __Ref__: +22; __Will__: +20 all-around vision"
hp: 250
health:
  - name: "HP"
    desc: "250; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]] 10"
abilities_mid:
  - name: "Skittering Reposition"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/move|move]])"
  - name: "Trigger"
    desc: "A creature that starts its move outside the gogiteth's reach moves into its reach"
  - name: "Effect"
    desc: "The gogiteth moves 10 feet. This does not trigger reactions."
speed: "40 feet, climb 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +26 __Damage__ 3d10+12 piercing plus Improved Grab"
  - name: "Melee"
    desc: "⬻ leg +26 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 3d6+12 piercing"
abilities_bot:
  - name: "Carry Off Prey"
    desc: "The gogiteth can move at its full Speed while it has a creature [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] in its jaws, bringing the grabbed creature along. __Constrict 3d6+12 bludgeoning, DC 32__ ⬻"
  - name: "Skittering Assault"
    desc: "⬺ The gogiteth Strides three times. Once per Stride, it can attempt a leg Strike against a creature in its reach at any point during the Stride; it must make each attack against a different creature, but it doesn't apply its multiple attack penalty until after making all its Strikes. If the result of any of the Strikes is a critical failure, Skittering Assault ends. Great Gogiteths As deadly as gogiteths are, rumors persist of even more terrifying threats known as great gogiteths. Said to be nearly a hundred feet across and capable of spawning their own hordes of gogiteths in reaction to being attacked, great gogiteths are also reputed to be unusually intelligent. The rumors claim that great gogiteths are largely content to lurk in their deep, remote caverns, spending ages dreaming of sadism and violence."
sourcebook: "_Monster Core_, page 177."
```

```encounter-table
name: Gogiteth
creatures:
  - 1: Gogiteth
```
