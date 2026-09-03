---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Adult Requiem Dragon"
tags:
  - pf2e/creature/level/15
  - pf2e/creature/trait/divine
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/huge
statblock: inline
name: "Adult Requiem Dragon"
level: 15
source: "Monster Core 2"
aon_id: "creature-4358"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4358"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Adult Requiem Dragon"
level: "Creature 15"
size: "Huge"
trait_01: "Divine"
trait_02: "Dragon"
modifier: 29
perception:
  - name: "Perception"
    desc: "Perception +29; darkvision, lifesense 90 feet, scent (imprecise) 60 feet, status sight"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/languages#Common|Common]], Daemonic, [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/languages#Empyrean|Empyrean]], Requian"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +25, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +30, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +27, [[srd/pf2e/compendium/rules-elements/skills/medicine|Medicine]] +33, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +30, [[srd/pf2e/compendium/rules-elements/skills/lore|River of Souls Lore]] +27"
abilityMods: [8, 5, 6, 5, 8, 6]
abilities_top:
  - name: "Soul Journey"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/exploration|exploration]]) The dragon spends 1 hour traveling through planar channels to reach the River of Souls, and then reaches any point along the river. This has the effects of [[srd/pf2e/compendium/spells/rank-7/interplanar-teleport|_interplanar teleport_]], except that the dragon can arrive precisely where they like on any major plane."
  - name: "Status Sight"
    desc: "The requiem dragon automatically knows the Hit Points of all creatures they can see."
ac: 36
armorclass:
  - name: "AC"
    desc: "36; __Fort__: +26; __Ref__: +23; __Will__: +29"
hp: 270
health:
  - name: "HP"
    desc: "270; __Immunities__ [[srd/pf2e/books/player-core/chapter-8-playing-the-game/hit-points-healing-and-dying#Death Effects|death effects]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]"
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
    desc: "The dragon resists the loosening of its own soul, preventing some of the damage. The dragon gains [[srd/pf2e/books/player-core/chapter-8-playing-the-game/immunity-weakness-and-resistance#Resistance|resistance]] 15 to all damage against the triggering attack."
speed: "50 feet, fly 150 feet, swim 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ horn +30 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 3d10+12 piercing plus 2d8 spirit"
  - name: "Melee"
    desc: "⬻ claw +30 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 10 feet]]) __Damage__ 3d6+12 slashing plus 2d8 spirit and Grab"
  - name: "Melee"
    desc: "⬻ tail +28 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]]) __Damage__ 3d8+12 bludgeoning plus 2d8 spirit"
abilities_bot:
  - name: "Dooming Breath"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/spirit|spirit]]) Energy from Creation's Forge erupts from the dragon's mouth, dealing 12d8 spirit damage in a 90-foot [[srd/pf2e/books/player-core/chapter-8-playing-the-game/area#Line|line]] (DC 36 [[srd/pf2e/books/player-core/chapter-8-playing-the-game/checks#Basic Saving Throws|basic]] Reflex save). Undead creatures who fail the save must also succeed at a DC 36 Will save or become [[srd/pf2e/compendium/rules-elements/conditions#Doomed|doomed]] 1. If the target is already doomed, the doomed value increases by 1 (to a maximum of doomed 4). The dragon can't use Dooming Breath again for 1d4 rounds."
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw strikes and one tail strike in any order."
  - name: "Draconic Momentum"
    desc: "The dragon recharges their Dooming Breath whenever they score a critical hit with a Strike."
  - name: "Soul Shield"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]])"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The requiem dragon uses their life essence to create a shield of spiritual energy around a creature within 60 feet. The shield creates a link between the dragon and the creature with the effects of share life except that the effect doesn't end regardless of distance and remains for 1 hour. In addition, the creature gains [[srd/pf2e/books/player-core/chapter-8-playing-the-game/immunity-weakness-and-resistance#Resistance|resistance]] 5 to physical and [[srd/pf2e/compendium/rules-elements/traits/player-core/spirit|spirit]] damage that applies to the half of damage it receives. The dragon can [[srd/pf2e/compendium/rules-elements/actions/player-core#Dismiss|Dismiss]] the effect."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 33 - __Cantrips (7th)__ [[srd/pf2e/compendium/spells/cantrips/stabilize|Stabilize]] - __6th__ [[srd/pf2e/compendium/spells/rank-1/heal|Heal]] (×3) - __7th__ [[srd/pf2e/compendium/spells/rank-1/heal|Heal]] (×2)"
sourcebook: "_Monster Core 2_, page 127."
```

```encounter-table
name: Adult Requiem Dragon
creatures:
  - 1: Adult Requiem Dragon
```
