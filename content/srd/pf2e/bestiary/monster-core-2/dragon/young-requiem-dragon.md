---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Young Requiem Dragon"
tags:
  - pf2e/creature/level/11
  - pf2e/creature/trait/divine
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/large
statblock: inline
name: "Young Requiem Dragon"
level: 11
source: "Monster Core 2"
aon_id: "creature-4357"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4357"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Young Requiem Dragon"
level: "Creature 11"
size: "Large"
trait_01: "Divine"
trait_02: "Dragon"
modifier: 24
perception:
  - name: "Perception"
    desc: "Perception +24; darkvision, lifesense 60 feet, scent (imprecise) 60 feet, status sight"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/languages#Common|Common]], Daemonic, [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/languages#Empyrean|Empyrean]], Requian"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +19, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +23, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +21, [[srd/pf2e/compendium/rules-elements/skills/medicine|Medicine]] +26, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +23, [[srd/pf2e/compendium/rules-elements/skills/lore|River of Souls Lore]] +21"
abilityMods: [7, 4, 5, 4, 7, 5]
abilities_top:
  - name: "Soul Journey"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/exploration|exploration]]) The dragon spends 1 hour traveling through planar channels to reach the River of Souls, and then reaches any point along the river. This has the effects of [[srd/pf2e/compendium/spells/rank-7/interplanar-teleport|_interplanar teleport_]], except that the dragon can arrive precisely where they like on any major plane."
  - name: "Status Sight"
    desc: "The requiem dragon automatically knows the Hit Points of all creatures they can see."
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +21; __Ref__: +18; __Will__: +24 +2 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]]"
hp: 190
health:
  - name: "HP"
    desc: "190; __Immunities__ [[srd/pf2e/books/player-core/chapter-8-playing-the-game/hit-points-healing-and-dying#Death Effects|death effects]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]"
abilities_mid:
  - name: "Soul Anchor"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]])"
  - name: "Trigger"
    desc: "A creature within 60 feet would drop to 0 Hit Points"
  - name: "Effect"
    desc: "The dragon anchors the triggering creature's soul to its body. The creature remains at 1 Hit Point, becomes [[srd/pf2e/compendium/rules-elements/conditions#Doomed|doomed]] 2, and gains fast healing equal to the dragon's level for 1 minute. The creature becomes temporarily immune to further Soul Anchor usages for 24 hours."
  - name: "Withhold Death"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]])"
  - name: "Trigger"
    desc: "The dragon is critically hit by an attack"
  - name: "Effect"
    desc: "The dragon resists the loosening of its own soul, preventing some of the damage. The dragon gains [[srd/pf2e/books/player-core/chapter-8-playing-the-game/immunity-weakness-and-resistance#Resistance|resistance]] 10 to all damage against the triggering attack."
speed: "40 feet, fly 120 feet, swim 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ horn +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 2d10+10 piercing plus 1d8 spirit"
  - name: "Melee"
    desc: "⬻ claw +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]]) __Damage__ 2d8+10 slashing plus 1d8 spirit and Grab"
  - name: "Melee"
    desc: "⬻ tail +22 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 2d8+10 bludgeoning plus 1d8 spirit"
abilities_bot:
  - name: "Dooming Breath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/spirit|spirit]]) Energy from Creation's Forge erupts from the dragon's mouth, dealing 9d8 spirit damage in a 60-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Line|line]] (DC 30 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save). Undead creatures who fail the save must also succeed at a DC 30 Will save or become [[srd/pf2e/compendium/rules-elements/conditions#Doomed|doomed]] 1. If the target is already doomed, the doomed value increases by 1 (to a maximum of doomed 4). The dragon can't use Dooming Breath again for 1d4 rounds."
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw strikes and one tail strike in any order."
  - name: "Draconic Momentum"
    desc: "The dragon recharges their Dooming Breath whenever they score a critical hit with a Strike."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 27 - __Cantrips (5th)__ [[srd/pf2e/compendium/spells/cantrips/stabilize|Stabilize]] - __4th__ [[srd/pf2e/compendium/spells/rank-1/heal|Heal]] (×3) - __5th__ [[srd/pf2e/compendium/spells/rank-1/heal|Heal]] (×2)"
sourcebook: "_Monster Core 2_, page 126."
```

```encounter-table
name: Young Requiem Dragon
creatures:
  - 1: Young Requiem Dragon
```
