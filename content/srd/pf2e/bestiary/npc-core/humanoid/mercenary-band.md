---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Mercenary Band"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/troop
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Mercenary Band"
level: 9
source: "NPC Core"
aon_id: "creature-3518"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3518"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Mercenary Band"
level: "Creature 9"
size: "Gargantuan"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Troop"
modifier: 17
perception:
  - name: "Perception"
    desc: "Perception +17"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Athletics +19, Intimidation +18, Military Lore +14, Society +14, Survival +15, Thievery +19"
abilityMods: [4, 2, 3, -1, 2, 1]
ac: 26
armorclass:
  - name: "AC"
    desc: "26; __Fort__: +18; __Ref__: +17; __Will__: +15"
hp: 180
health:
  - name: "HP"
    desc: "180; __Weaknesses__ area damage 10, splash damage 10"
abilities_mid:
  - name: "Troop Defenses"
    desc: ""
speed: "25 feet; troop movement"
abilities_bot:
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The mercenary band engages in a coordinated attack with its wide array of melee weapons against each enemy in a 5-foot emanation with a DC 25 basic Reflex save. The damage depends on the number of actions. ⬻ 1d8+2 bludgeoning, piercing, or slashing ⬺ 3d8+4 bludgeoning, piercing, or slashing ⬽ 4d8+6 bludgeoning, piercing, or slashing __Ready… Fire!__ ⬺ The mercenary band draws or reloads their bows, crossbows, and slings, then launches a ranged attack in the form of a volley. This volley is a 10-foot burst within 120 feet that deals 2d8+4 piercing or bludgeoning damage with a DC 25 basic Reflex save. When the mercenary band is reduced to 2 or fewer segments, this area decreases to a 5-foot burst."
  - name: "Spoils of War"
    desc: "⬻"
  - name: "Requirements"
    desc: "The band's last action was Let 'em Have It and at least one creature failed its save"
  - name: "Effect"
    desc: "The mercenary band attempts to Steal one object from each enemy that failed its save, even if the enemy is in combat or on guard."
sourcebook: "_NPC Core_, page 84."
```

```encounter-table
name: Mercenary Band
creatures:
  - 1: Mercenary Band
```
