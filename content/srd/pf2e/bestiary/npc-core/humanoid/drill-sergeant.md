---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Drill Sergeant"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Drill Sergeant"
level: 8
source: "NPC Core"
aon_id: "creature-3529"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3529"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Drill Sergeant"
level: "Creature 8"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Athletics +18, Intimidation +20, Warfare Lore +18"
abilityMods: [4, 3, 2, 2, 2, 4]
abilities_top:
  - name: "Items"
    desc: "Chain Shirt, Javelin (6), _+1 striking longsword_"
ac: 25
armorclass:
  - name: "AC"
    desc: "25; __Fort__: +14; __Ref__: +15; __Will__: +20"
hp: 120
health:
  - name: "HP"
    desc: "120"
abilities_mid:
  - name: "Commanding Aura"
    desc: "(aura, emotion, mental, visual) 60 feet. An ally that starts its turn in the aura gains 8 temporary Hit Points. These last until the start of the creature's next turn. __You Don't Have My Permission to Die!__ ⬲ (auditory, emotion, fear, linguistic, mental)"
  - name: "Trigger"
    desc: "An allied creature within 30 feet would be reduced to 0 Hit Points"
  - name: "Effect"
    desc: "With a stern rebuke, the drill sergeant berates the target for their failure. The creature avoids being knocked out and remains at 1 HP. The creature is then temporarily immune for 24 hours."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _longsword_ +21 (Magical, versatile P) __Damage__ 2d8+12 slashing"
  - name: "Melee"
    desc: "⬻ fist +20 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+12 bludgeoning"
  - name: "Ranged"
    desc: "⬻ javelin +19 (thrown 30 feet) __Damage__ 1d6+12 piercing"
abilities_bot:
  - name: "Chastising Enforcement"
    desc: "⬻ (Auditory, Emotion, Linguistic, Mental) The drill sergeant exhorts a faltering comrade with a stern word and attempts an Intimidation check against the Will DC of one ally within 30 feet. On a success, the target's frightened condition is reduced by 2 and the drill sergeant can attempt to counteract one mental effect that ally is suffering from with a +18 counteract modifier. On a critical success, the drill sergeant also reduces the frightened condition of each other ally in a 10-foot emanation around the target by 1. __Keep Up With Me!__ ⬻ (Auditory, Emotion, Linguistic, Mental)"
  - name: "Requirements"
    desc: "The drill sergeant's last action was a Strike that hit"
  - name: "Effect"
    desc: "The drill sergeant shouts that one ally within 30 feet can't keep up with them. That ally gains a +3 status bonus to their attack roll on the next Strike they make before the start of the drill sergeant's next turn. If the ally is a troop, this bonus instead applies to the DC of their next offensive activity (such as Join the Fray for heavy cavalry)."
sourcebook: "_NPC Core_, page 93."
```

```encounter-table
name: Drill Sergeant
creatures:
  - 1: Drill Sergeant
```
