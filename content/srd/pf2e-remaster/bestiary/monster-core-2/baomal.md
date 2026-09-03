---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Baomal"
tags:
  - pf2e/creature/level/20
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/aquatic
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Baomal"
level: 20
source: "Monster Core 2"
aon_id: "creature-4278"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4278"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Baomal"
level: "Creature 20"
size: "Gargantuan"
trait_01: "Aberration"
trait_02: "Aquatic"
modifier: 34
perception:
  - name: "Perception"
    desc: "Perception +34; darkvision, scent (imprecise) 80 feet"
languages: "Aklo"
skills:
  - name: "Skills"
    desc: "Athletics +34, Stealth +31, Survival +37"
abilityMods: [10, 2, 8, -3, 6, 1]
ac: 46
armorclass:
  - name: "AC"
    desc: "46; __Fort__: +36; __Ref__: +30; __Will__: +34"
hp: 315
health:
  - name: "HP"
    desc: "315; __Resistances__ physical 10"
abilities_mid:
  - name: "All-Around Vision"
    desc: ""
  - name: "Reactive Strike"
    desc: "⬲"
  - name: "Doubled Reaction"
    desc: "A baomal gains an extra reaction each round that it can use only to make a Reactive Strike. It must use a different head for each one it attempts, and it can't make more than one Reactive Strike for the same triggering action."
  - name: "Psychic Static Aura"
    desc: "(aura, mental, occult) 120 feet. All creatures, except aberrations, that begin their turn in the area take 5d6 mental damage."
  - name: "Two Heads"
    desc: "Any ability that would sever a baomal's head (such as a critical hit with a _vorpal_ weapon) severs one head at random. Losing one head doesn't kill a baomal, but it does prevent the baomal from making Strikes with the lost head and from using Doubled Reaction or Two-Headed Strike."
speed: "50 feet, swim 80 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +38 (reach 20 feet) __Damage__ 4d12+18 piercing plus Improved Grab"
  - name: "Ranged"
    desc: "⬻ tsunami jet +38 (Brutal, range 500 feet) __Damage__ 4d10+18 bludgeoning plus Push 40 feet"
abilities_bot:
  - name: "Breath of the Sea"
    desc: "⬻ (Attack) A baomal can inhale tremendous amounts of water, drawing everything in the sea nearby closer. All creatures and objects in the water within 60 feet of the baomal (including ships) are pulled toward it. Creatures must succeed at a DC 42 Athletics check or be pulled up to 20 feet toward the baomal (40 feet on a critical failure). For ships, use the captain's Sailing Lore in place of Athletics. Unattended objects are automatically pulled."
  - name: "Shell Rake"
    desc: "⬻ The baomal Swims or Strides alongside a creature or the hull of a vessel, dealing damage with the strong spikes on its shell. Each creature or ship the baomal is adjacent to at any point during its movement takes 6d6+10 slashing and piercing damage (DC 42 basic Reflex save). Against vessels, Shell Rake ignores the first 5 Hardness and creates an explosion of splinters that deals 3d6+5 damage to every creature within 10 feet of the deck's edge (DC 42 basic Reflex save)."
  - name: "Two-Headed Strike"
    desc: "⬺ The baomal makes a Strike with each set of jaws, each against a different creature. These Strikes count as one attack for the baomal's multiple attack penalty, and the penalty doesn't increase until after both attacks. Mysterious Origins All too often, those who study strange monsters assume they were created by powerful but ill-advised wizards or that they're the result of the alghollthu empire's ancient experiments. In the case of the baomal, extensive research suggests that neither of these explanations are accurate. No ancient texts have been recovered in which a wizard claims to have created the first baomal, and while the alghollthu use them as warbeasts, ancient carvings suggest that, in the earliest days, baomals ravenously hunted alghollthus."
sourcebook: "_Monster Core 2_, page 55."
```

```encounter-table
name: Baomal
creatures:
  - 1: Baomal
```
