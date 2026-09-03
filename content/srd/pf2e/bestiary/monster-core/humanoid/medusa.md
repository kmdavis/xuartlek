---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Medusa"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Medusa"
level: 7
source: "Monster Core"
aon_id: "creature-3096"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3096"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Medusa"
level: "Creature 7"
size: "Medium"
trait_01: "Humanoid"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16; darkvision"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Deception +16, Diplomacy +14, Stealth +16"
abilityMods: [2, 5, 4, 2, 1, 2]
abilities_top:
  - name: "Items"
    desc: "_+1 composite shortbow_ (60 arrows), Shortsword"
ac: 25
armorclass:
  - name: "AC"
    desc: "25; __Fort__: +15; __Ref__: +16; __Will__: +14"
hp: 105
health:
  - name: "HP"
    desc: "105"
abilities_mid:
  - name: "Petrifying Gaze"
    desc: "(arcane, aura, visual) 30 feet. When a creature ends its turn in the aura, it must attempt a DC 25 Fortitude save. If the creature fails, it becomes slowed 1 for 1 minute. The medusa can deactivate or activate this aura by using a single action, which has the concentrate trait."
  - name: "Biting Snakes"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature ends its turn adjacent to the medusa"
  - name: "Effect"
    desc: "The medusa makes a snake fangs Strike against the creature."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ shortsword +18 (Agile, Finesse, versatile S) __Damage__ 1d6+8 piercing plus serpent venom"
  - name: "Melee"
    desc: "⬻ snake fangs +16 (Agile, Finesse) __Damage__ 1d4+8 piercing plus serpent venom"
  - name: "Ranged"
    desc: "⬻ _composite shortbow_ +19 (deadly d10, Magical, Propulsive, range increment 60 feet, reload 0) __Damage__ 1d6+7 piercing plus serpent venom"
abilities_bot:
  - name: "Focus Gaze"
    desc: "⬻ (Arcane, Concentrate, Incapacitation, Visual) The medusa fixes their glare at a creature they can see within 30 feet. The target must immediately attempt a Fortitude save against the medusa's petrifying gaze. If the creature was already slowed by petrifying gaze before attempting its save, a failed save causes it to be petrified permanently. After attempting its save, the creature is then temporarily immune until the start of the medusa's next turn."
  - name: "Serpent Venom"
    desc: "(Poison)"
  - name: "Saving Throw"
    desc: "DC 25 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "1d6 poison damage and enfeebled 1 (1 round)"
  - name: "Stage 2"
    desc: "2d6 poison damage and enfeebled 2 (1 round) Medusa Infiltrators Rumors persist of disguised medusas acting as prominent members of criminal organizations such as the Sczarni in Riddleport and the Aspis Consortium in Port Peril, and their kind is known to thrive in metropolises including Absalom and Katapesh. Because they are so widespread, medusas resembling humans of every major ethnicity can be found in Avistan and Garund."
sourcebook: "_Monster Core_, page 230."
```

```encounter-table
name: Medusa
creatures:
  - 1: Medusa
```
