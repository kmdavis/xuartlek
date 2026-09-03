---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Shotalashu"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/large
statblock: inline
name: "Shotalashu"
level: 2
source: "Howl of the Wild"
aon_id: "creature-3309"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3309"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Shotalashu"
level: "Creature 2"
size: "Large"
trait_01: "Beast"
trait_02: "Uncommon"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Elven|Elven]], [[srd/pf2e/compendium/rules-elements/languages#Lashunta|Lashunta]]; (can't speak any language); empathic communication"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +8, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +8, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +8, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +7"
abilityMods: [2, 4, 2, -3, 3, 2]
abilities_top:
  - name: "Empathic Communication"
    desc: "While a shotalashu can't speak, even telepathically, it understands simple commands in the languages it knows. It returns telepathic sensations of emotion to creatures touching it or the partner of its telepathic link at any distance."
  - name: "Telepathic Link"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]]) A rider who would tame a shotalashu for a mount must first form a telepathic link with it. Establishing this link require spending a week with the desired mount and succeeding at a DC 21 [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] check. Any creature with telepathic capabilities, such as telepathy, touch telepathy, empathic sense, or the ability to cast spells such as [[srd/pf2e/compendium/spells/rank-4/telepathy|_telepathy_]], gains a +4 circumstance bonus to this check. This link remains and neither can form a new link until one member dies. The shock of a partner dying leaves the survivor [[srd/pf2e/compendium/rules-elements/conditions#Stupefied|stupefied 2]] for 24 hours and prevents forming a new link for at least a month."
ac: 18
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +8; __Ref__: +10; __Will__: +11"
hp: 35
health:
  - name: "HP"
    desc: "35"
speed: "40 feet, jungle stride"
attacks:
  - name: "Melee"
    desc: "⬻ claws +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 1d6+2 slashing plus 1d4 mental"
abilities_bot:
  - name: "Jungle Stride"
    desc: "The shotalashu ignores difficult terrain due to vegetation."
  - name: "Telepathic Pounce"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|Occult]]) The shotalashu hunts by pinning its foes with its mind. One creature within 30 feet must attempt a DC 18 Will save."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature takes a –5 foot status penalty to its Speeds for one round."
  - name: "Failure"
    desc: "The creature takes a –10 foot status penalty to its Speeds for one round. The shotalashu can then [[srd/pf2e/compendium/rules-elements/actions/player-core#Leap|Leap]]."
  - name: "Critical Failure"
    desc: "The creature is [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] and [[srd/pf2e/compendium/rules-elements/conditions#Immobilized|immobilized]] for one round. The shotalashu can Leap."
sourcebook: "_Howl of the Wild_, page 180."
```

```encounter-table
name: Shotalashu
creatures:
  - 1: Shotalashu
```
