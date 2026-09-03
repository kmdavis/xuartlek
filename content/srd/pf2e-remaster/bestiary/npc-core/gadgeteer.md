---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Gadgeteer"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Gadgeteer"
level: 6
source: "NPC Core"
aon_id: "creature-3462"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3462"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Gadgeteer"
level: "Creature 6"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Crafting +16, Engineering Lore +18, Society +12, Thievery +14"
abilityMods: [1, 4, 1, 4, 2, 0]
abilities_top:
  - name: "Gadget Specialist"
    desc: "For encounters involving crafting gadgets, the gadgeteer is a 9th-level challenge."
  - name: "Items"
    desc: "bag of junk, Crossbow (10 bolts), heavy wrench (functions as a mace), Leather Armor"
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +11; __Ref__: +16; __Will__: +14"
hp: 95
health:
  - name: "HP"
    desc: "95"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +16 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+7 bludgeoning"
  - name: "Melee"
    desc: "⬻ heavy wrench +13 (Shove) __Damage__ 1d6+7 bludgeoning"
  - name: "Ranged"
    desc: "⬻ crossbow +16 (range increment 120 feet, reload 1) __Damage__ 1d8+6 piercing"
abilities_bot:
  - name: "Create Gadget"
    desc: "⬽ (Concentrate, Manipulate) The gadgeteer uses their bag of junk and nearby scraps to create one of the following gadgets. Gadgets created this way fall apart after a single use or after 1 hour, whichever happens first."
  - name: "Flash Bang"
    desc: "⬻ (manipulate) The gadgeteer throws a flash bang up to 20 feet away that explodes in a 5-foot burst. Creatures in the burst must succeed a DC 24 Fortitude save or become blinded for 1 round."
  - name: "Glider"
    desc: "⬻ (move) The gadgeteer leaps off a precipice with the glider in their hands. They fall only 60 feet per round, and for every 10 feet they fall, they can travel 5 feet forward."
  - name: "Makeshift Key"
    desc: "⬻ (manipulate) The gadgeteer attempts to Pick a Lock with a +4 item bonus to the check."
  - name: "Recorder"
    desc: "⬻ (manipulate) The gadgeteer records up to 25 spoken words on this device. Activating this gadget causes it to either repeat the recorded words once before falling apart or play the message on a loop for up to 10 minutes before falling apart."
  - name: "Shocking Rod"
    desc: "⬻ (manipulate) An adjacent creature takes 3d12 electricity damage with a DC 24 basic Reflex save."
sourcebook: "_NPC Core_, page 46."
```

```encounter-table
name: Gadgeteer
creatures:
  - 1: Gadgeteer
```
