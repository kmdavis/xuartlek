---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Scarecrow"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/construct
  - pf2e/creature/trait/medium
statblock: inline
name: "Scarecrow"
level: 4
source: "Monster Core"
aon_id: "creature-3174"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3174"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Scarecrow"
level: "Creature 4"
size: "Medium"
trait_01: "Construct"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; darkvision"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +12"
abilityMods: [5, 2, 3, -4, 3, -2]
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +13; __Ref__: +8; __Will__: +11"
hp: 60
health:
  - name: "HP"
    desc: "60; __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/traits/player-core/death|death]] effects, [[srd/pf2e/compendium/rules-elements/traits/player-core/disease|disease]], [[srd/pf2e/compendium/rules-elements/conditions#Doomed|doomed]], [[srd/pf2e/compendium/rules-elements/conditions#Drained|drained]], [[srd/pf2e/compendium/rules-elements/conditions#Fatigued|fatigued]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/healing|healing]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|nonlethal]] attacks, [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], poison, [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened]], [[srd/pf2e/compendium/rules-elements/traits/player-core/spirit|spirit]], [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]], [[srd/pf2e/compendium/rules-elements/traits/player-core/vitality|vitality]], [[srd/pf2e/compendium/rules-elements/traits/player-core/void|void]]; __Resistances__ physical 5 (except slashing); __Weaknesses__ fire 5"
abilities_mid:
  - name: "Scarecrow's Leer"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/emotion|emotion]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|visual]]) 40 feet. The scarecrow's eyes flicker with an unnerving glow. A creature can't reduce its [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened]] condition below 1 as long as it's in the aura. When a creature enters or starts its turn in the aura, it must attempt a DC 18 Will save. Birds and other avian creatures take a –2 circumstance penalty to this save."
  - name: "Critical Success"
    desc: "The creature is unaffected and is then temporarily immune for 24 hours."
  - name: "Success"
    desc: "The creature is frightened 1."
  - name: "Failure"
    desc: "The creature is frightened 2 and is [[srd/pf2e/compendium/rules-elements/conditions#Fascinated|fascinated]] by the scarecrow until the end of its next turn."
  - name: "Critical Failure"
    desc: "As failure, but frightened 3."
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +13 ([[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 2d6+7 bludgeoning plus clawing fear"
abilities_bot:
  - name: "Baleful Glow"
    desc: "⭓ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/light|Light]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|Occult]]) The scarecrow's head bursts into ghostly, heatless flame that sheds bright light in a 20-foot emanation (and dim light to the next 20 feet). If the scarecrow uses this ability on the first round of combat, any creature that has not acted yet is startled, becoming [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] against the scarecrow for 1 round. The scarecrow can suppress the light by using this action again."
  - name: "Clawing Fear"
    desc: "The scarecrow's strikes deal an additional 1d6 mental damage to [[srd/pf2e/compendium/rules-elements/conditions#Frightened|frightened]] creatures."
  - name: "Mundane Appearance"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]]) Until it acts, the scarecrow resembles an ordinary scarecrow. It has an automatic result of 32 on [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] checks and DCs to pass as an ordinary scarecrow. Odds and Ends Scarecrows hold a certain liminal space that is inhabitable by spirit creatures. [[srd/pf2e/compendium/gm/creature-families/ghost|Ghosts]] in particular can use their malevolent possession on a scarecrow as if it were a living creature, using them as vehicles to escape their site-bound nature and so further spread their murder and mayhem."
sourcebook: "_Monster Core_, page 297."
```

```encounter-table
name: Scarecrow
creatures:
  - 1: Scarecrow
```
