---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Shikigami"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/kami
  - pf2e/creature/trait/spirit
  - pf2e/creature/trait/tiny
statblock: inline
name: "Shikigami"
level: 1
source: "Monster Core 2"
aon_id: "creature-4453"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4453"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Shikigami"
level: "Creature 1"
size: "Tiny"
trait_01: "Kami"
trait_02: "Spirit"
modifier: 9
perception:
  - name: "Perception"
    desc: "Perception +9; darkvision"
languages: "Common, Empyrean"
skills:
  - name: "Skills"
    desc: "Diplomacy +6, Medicine +7, Nature +7, Society +6, Stealth +7"
abilityMods: [2, 2, 3, 1, 4, 3]
abilities_top:
  - name: "Ward"
    desc: "(divine) Every kami is bound to a ward: a specific animal, plant, object, or location. A kami can merge with or emerge from their ward as a single action, which has the concentrate trait. While merged, the kami can observe their surroundings with their usual senses as well as the senses of their ward, but can't move, communicate with, or control their ward. Additionally, a kami merged with their ward recovers Hit Points each minute as if they spent an entire day resting. A shikigami's ward is typically a minor work of art or symbol of civilization, such as a milestone, trail sign, personal garden, or tiny statue."
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +7; __Ref__: +6; __Will__: +9"
hp: 18
health:
  - name: "HP"
    desc: "18; __Immunities__ bleed; __Weaknesses__ cold iron 3"
speed: "20 feet; flatten"
attacks:
  - name: "Melee"
    desc: "⬻ spade +7 (Agile, versatile S) __Damage__ 1d6+2 piercing"
  - name: "Melee"
    desc: "⬻ fist +7 (Agile) __Damage__ 1d4+2 bludgeoning"
  - name: "Ranged"
    desc: "⬻ spade +7 (Agile, thrown 10 feet, versatile S) __Damage__ 1d6+2 piercing"
abilities_bot:
  - name: "Innate Divine Spells"
    desc: "DC 17 - __Cantrips (1st)__ Forbidding Ward - __1st__ Cleanse Cuisine - __2nd__ Animal Messenger, Invisibility (self only)"
  - name: "Flatten"
    desc: "⭓ The shikigami flattens to the width of a sheet of paper. While Flattened, they can float on the wind, gaining a 20-foot fly Speed, and they can slip through small cracks and gaps without needing to Squeeze; however, they become clumsy 2. The shikigami can Dismiss this effect."
sourcebook: "_Monster Core 2_, page 204."
```

```encounter-table
name: Shikigami
creatures:
  - 1: Shikigami
```
