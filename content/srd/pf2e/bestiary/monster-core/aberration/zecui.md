---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Zecui"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/medium
statblock: inline
name: "Zecui"
level: 6
source: "Monster Core"
aon_id: "creature-3248"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3248"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Zecui"
level: "Creature 6"
size: "Medium"
trait_01: "Aberration"
trait_02: "Uncommon"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Aklo|Aklo]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +17, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +15, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +12, [[srd/pf2e/compendium/rules-elements/skills/medicine|Medicine]] +14, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +17"
abilityMods: [3, 5, 2, 0, 2, 0]
abilities_top:
  - name: "Items"
    desc: "Shortsword (2)"
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +14; __Ref__: +17; __Will__: +12"
hp: 110
health:
  - name: "HP"
    desc: "110"
abilities_mid:
  - name: "Preserve Prey"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/healing|healing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/manipulate|manipulate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|vitality]])"
  - name: "Trigger"
    desc: "A living creature within 30 feet is reduced to 0 Hit Points"
  - name: "Effect"
    desc: "The zecui channels corrupt vitality into the triggering creature, which still goes [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]] but does not gain the [[srd/pf2e/compendium/rules-elements/conditions#Dying|dying]] condition. While that creature is unconscious, the residual energy attempts to counteract any [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|vitality]] spell healing that creature with a +15 counteract modifier."
speed: "30 feet, burrow 20 feet, climb 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ mandibles +15 __Damage__ 2d8+7 piercing"
  - name: "Melee"
    desc: "⬻ shortsword +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 2d6+7 piercing"
  - name: "Melee"
    desc: "⬻ claws +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 2d4+7 slashing plus Grab"
  - name: "Ranged"
    desc: "⬻ spit +17 (range 30 feet) __Damage__ spit mucus"
abilities_bot:
  - name: "Dual Stab"
    desc: "⬻"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The zecui makes two shortsword Strikes against an [[srd/pf2e/compendium/rules-elements/conditions#Immobilized|immobilized]] or [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] target. These strikes count towards the zecui's multiple attack penalty, but it doesn't increase until after the second attack."
  - name: "Harden Chitin"
    desc: "⬻ The zecui fuses much of their chitin into a black metallic shell. They gain resistance 5 to all damage (except [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]] and [[srd/pf2e/compendium/rules-elements/traits/player-core/spirit|spirit]]) until they next take a [[srd/pf2e/compendium/rules-elements/traits/player-core/move|move]] action."
  - name: "Spit Mucus"
    desc: "A creature hit by the zecui's spit attack is [[srd/pf2e/compendium/rules-elements/conditions#Immobilized|immobilized]] by the larva-infested mucus and stuck to the nearest surface until it [[srd/pf2e/compendium/rules-elements/actions/player-core#Escape|Escapes]] (DC 25). While that creature is immobilized, it is exposed to zecui larvae at the end of each of its turns."
  - name: "Zecui Larvae"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/disease|Disease]])"
  - name: "Saving Throw"
    desc: "DC 25 Fortitude"
  - name: "Stage 1"
    desc: "visible lumps as the larvae move but no ill effect (1 day)"
  - name: "Stage 2"
    desc: "[[srd/pf2e/compendium/rules-elements/conditions#Drained|drained 1]] (1 day)"
  - name: "Stage 3"
    desc: "drained 2 (1 day)"
  - name: "Stage 4"
    desc: "drained 3 and [[srd/pf2e/compendium/rules-elements/conditions#Controlled|controlled]] by the zecui larva (1 day)"
  - name: "Stage 5"
    desc: "the creature dies and the adult zecui can emerge from the corpse as an Interact action The Dark Brood Although zecuis generally operate in personal nests, a coalition of zecui thrives in the Valashmai Jungle of Tian Xia, nesting in the ruins of the ancient empire that attempted to control their ancestors. Recently, the brood has turned its gaze outwards, building up numbers to begin a great expansion."
sourcebook: "_Monster Core_, page 355."
```

```encounter-table
name: Zecui
creatures:
  - 1: Zecui
```
