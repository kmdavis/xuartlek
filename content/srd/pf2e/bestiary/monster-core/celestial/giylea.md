---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Giylea"
tags:
  - pf2e/creature/level/16
  - pf2e/creature/trait/archon
  - pf2e/creature/trait/celestial
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/huge
statblock: inline
name: "Giylea"
level: 16
source: "Monster Core"
aon_id: "creature-2836"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2836"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Giylea"
level: "Creature 16"
size: "Huge"
trait_01: "Archon"
trait_02: "Celestial"
trait_03: "Holy"
trait_04: "Rare"
modifier: 28
perception:
  - name: "Perception"
    desc: "Perception +28; darkvision, _truesight_"
languages: "Diabolic, Draconic, Empyrean, Utopian; _truespeech_"
skills:
  - name: "Skills"
    desc: "Acrobatics +31, Athletics +30, Intimidation +29, Religion +28, Warfare Lore +29"
abilityMods: [6, 9, 6, 5, 6, 3]
ac: 41
armorclass:
  - name: "AC"
    desc: "41; __Fort__: +26; __Ref__: +31; __Will__: +28 +1 status to all saves vs. magic"
hp: 230
health:
  - name: "HP"
    desc: "230; __Immunities__ fear; __Weaknesses__ unholy 15"
abilities_mid:
  - name: "All-Knowing Eyes"
    desc: "(aura, divine, mental, visual) 30 feet. When a creature ends its turn in the giylea's aura, it must attempt a DC 34 Will save. If the creature fails, any Deception check it attempts until the end of its next turn has its result reduced by one degree of success. If a creature is currently disguised or in a shape other than its true form when it fails its save, it also becomes stupefied 1 until the end of its next turn."
  - name: "Archon's Protection"
    desc: "⬲"
  - name: "Trigger"
    desc: "An enemy damages the archon's ally and both are within 15 feet of the archon"
  - name: "Effect"
    desc: "The ally gains resistance 20 to all damage against the triggering damage and the archon can make a Strike against the enemy."
speed: "fly 50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ slam +30 (Holy, Magical) __Damage__ 3d12+14 bludgeoning plus 1d6 fire"
  - name: "Ranged"
    desc: "⬻ tongue of flame +33 (Fire, Holy, Magical, range 30 feet) __Damage__ 7d6 fire"
abilities_bot:
  - name: "Fiery Spokes"
    desc: "⬺ (Divine, Fire, Holy, Spirit) The giylea spins furiously, emitting a rain of divine fire. All creatures in a 60-foot emanation take 12d6 fire damage and 5d6 spirit damage with a DC 37 basic Reflex save. The giylea can't use Fiery Spokes for 1d4 rounds."
  - name: "Focus Gaze"
    desc: "⬻ (Concentrate, Divine, Mental, Visual) The giylea fixes their gaze on a creature they can see within 30 feet. The target must immediately attempt a DC 37 Will save against the giylea's all-knowing eyes. If the creature is under any magical effect that disguises it or has altered its shape, the giylea attempts to counter that magical disguise effect (counteract +29, 8th rank). After attempting its save, the creature is then temporarily immune until the start of the giylea's next turn."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 37, attack +29 - __7th__ Divine Decree, Divine Immolation, Scouting Eye, Zealous Conviction - __8th__ Divine Wrath, Ring of Truth (at will) - __9th__ Detonate Magic - __Constant (8th)__ Ring of Truth, Truesight, Truespeech"
sourcebook: "_Monster Core_, page 29."
```

```encounter-table
name: Giylea
creatures:
  - 1: Giylea
```
