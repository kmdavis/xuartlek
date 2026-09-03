---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Cacodaemon"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/daemon
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/tiny
statblock: inline
name: "Cacodaemon"
level: 1
source: "Monster Core"
aon_id: "creature-2891"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2891"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Cacodaemon"
level: "Creature 1"
size: "Tiny"
trait_01: "Daemon"
trait_02: "Fiend"
trait_03: "Unholy"
modifier: 6
perception:
  - name: "Perception"
    desc: "Perception +6; darkvision"
languages: "Daemonic; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +8, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +5, [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] +6, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +8"
abilityMods: [0, 3, 2, -1, 1, 2]
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +7; __Ref__: +8; __Will__: +6"
hp: 22
health:
  - name: "HP"
    desc: "22; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/death|death]] effects; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|holy]] 3"
speed: "5 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|Disease]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 0 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|Unholy]]) __Damage__ 1d8 piercing plus cacodaemonia"
  - name: "Melee"
    desc: "⬻ jaws +8 (agile, finesse) __Damage__ 1d8+1 piercing"
  - name: "Melee"
    desc: "⬻ tentacle +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|finesse]]) __Damage__ 1d8+1 bludgeoning plus Grab (page 359)"
  - name: "Melee"
    desc: "⬻ beak +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|finesse]]) __Damage__ 1d6 piercing plus 2 poison"
  - name: "Melee"
    desc: "⬻ pincer +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|finesse]]) __Damage__ 1d6+1 bludgeoning plus Grab"
  - name: "Melee"
    desc: "stinger +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|finesse]]) __Damage__ 1d6+1 piercing plus 1d4 poison"
abilities_bot:
  - name: "Cacodaemonia"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/disease|Disease]]) The cacodaemon can telepathically communicate with the afflicted creature at any distance on the same plane"
  - name: "Saving Throw"
    desc: "DC 17 Fortitude"
  - name: "Stage 1"
    desc: "carrier (1 day)"
  - name: "Stage 2"
    desc: "[[srd/pf2e/compendium/rules-elements/conditions#Stupefied|stupefied 1]] (1 day)"
  - name: "Stage 3"
    desc: "stupefied 2 (1 day)"
  - name: "Change Shape"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/polymorph|Polymorph]])"
  - name: "Lizard"
    desc: "Speed 20 feet"
  - name: "Octopus"
    desc: "size Small; Speed 20 feet, swim 30 feet; Skills [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +6"
  - name: "Scorpion"
    desc: "size Small; Speed 30 feet; Skills [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +6"
  - name: "Soul Lock"
    desc: "⬽ ([[srd/pf2e/compendium/rules-elements/traits/player-core/death|Death]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]])"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The cacodaemon ingests the soul of a sentient creature within 30 feet that died within the last minute. When they do, the cacodaemon grows a fist-sized soul gem (Hardness 2, HP 8) in their gut and can regurgitate it at any time as an Interact action. Destroying the gem frees the soul within but doesn't return the deceased creature to life. If a caster attempts to return to life a creature whose soul is trapped within a soul gem, they fail unless they succeed at a DC 30 [[srd/pf2e/compendium/rules-elements/skills/religion|Religion]] check. A success causes the soul gem to shatter so the creature is returned to life as normal for the spell. A fiend can Interact to ingest a soul gem it is holding, condemning the soul to the fiend's home plane. The fiend gains fast healing 5 for 1 minute."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 17 - __Cantrips (1st)__ [[srd/pf2e/compendium/spells/cantrips/detect-magic|Detect Magic]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/fear|Fear]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/invisibility|Invisibility]] (at will; self only) - __4th__ [[srd/pf2e/compendium/spells/rank-4/read-omens|Read Omens]]"
sourcebook: "_Monster Core_, page 72."
```

```encounter-table
name: Cacodaemon
creatures:
  - 1: Cacodaemon
```
