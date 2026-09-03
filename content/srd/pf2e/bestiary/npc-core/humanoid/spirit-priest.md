---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Spirit Priest"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/dwarf
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Spirit Priest"
level: 5
source: "NPC Core"
aon_id: "creature-3627"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3627"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Spirit Priest"
level: "Creature 5"
size: "Medium"
trait_01: "Dwarf"
trait_02: "Humanoid"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12; darkvision"
languages: "Common, Dwarven, Empyrean, Fey, Petran, Pyric"
skills:
  - name: "Skills"
    desc: "Athletics +12, Diplomacy +12, Dwarf Lore +10, Occultism +10, Religion +14"
abilityMods: [2, 0, 3, 0, 5, 2]
abilities_top:
  - name: "Items"
    desc: "Clan Dagger"
ac: 19
armorclass:
  - name: "AC"
    desc: "19; __Fort__: +12; __Ref__: +9; __Will__: +14"
hp: 78
health:
  - name: "HP"
    desc: "78"
speed: "20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ clan dagger +11 (Agile, Parry, versatile B) __Damage__ 1d4+6 piercing"
  - name: "Melee"
    desc: "⬻ fist +11 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+6 bludgeoning"
abilities_bot:
  - name: "Spirit's Interference"
    desc: "⬺ The spirit priest calls out to a local spirit to assault the priest's enemies. The spirit unleashes a blast of rocks, attacks with a set of vines, or uses some other appropriate part of the environment to attack all creatures in a 10-foot burst within 30 feet of the priest. The attack deals 6d6 bludgeoning damage with a DC 18 basic Reflex save. The spirit priest can't use Spirit's Interference for 1d4 rounds. The GM might have this ability deal a different damage type based on the local spirits, such as fire damage when calling on a fire spirit."
  - name: "Spiritual Edge"
    desc: "⬻ (Concentrate, Spellshape, Spirit) The spirit priest aligns their spirit with their magical effects, enhancing the power of their spells. If their next action is to Cast a Spell that deals damage and doesn't have a duration, the spell deals additional spirit damage equal to the spell's rank."
spellcasting:
  - name: "Divine Spontaneous Spells"
    desc: "DC 22, attack +14 - __Cantrips (2nd)__ Detect Magic, Divine Lance, Guidance, Shield, Stabilize - __1st__ Bless, Fear, Infuse Vitality, Spirit Link (4 slots) - __2nd__ Augury, Heal, Noise Blast, See the Unseen (4 slots) - __3rd__ Noise Blast, Safe Passage, Spiritual Armament (3 slots)"
sourcebook: "_NPC Core_, page 174."
```

```encounter-table
name: Spirit Priest
creatures:
  - 1: Spirit Priest
```
