---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Anguished Flame"
tags:
  - pf2e/creature/level/13
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/fire
  - pf2e/creature/trait/light
  - pf2e/creature/trait/large
statblock: inline
name: "Anguished Flame"
level: 13
source: "Monster Core 2"
aon_id: "creature-4523"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4523"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Anguished Flame"
level: "Creature 13"
size: "Large"
trait_01: "Elemental"
trait_02: "Fire"
trait_03: "Light"
modifier: 28
perception:
  - name: "Perception"
    desc: "Perception +28"
languages: "Empyrean, Pyric; _truespeech_"
skills:
  - name: "Skills"
    desc: "Athletics +24, Crafting +27, Deity Lore +25, Diplomacy +27, Medicine +27, Nature +23, Plane of Fire Lore +25, Religion +23"
abilityMods: [5, 7, 5, 4, 6, 8]
abilities_top:
  - name: "Eternal Luminosity"
    desc: "(light) An anguished flame naturally sheds brilliant light like a torch. When other creatures target the anguished flame, they ignore the concealed condition from darkness, fog, mist, and smoke."
  - name: "Purifying Flame"
    desc: "An anguished flame can Treat Wounds without a healer's toolkit, instead healing the wounded with the gentle light of their touch."
ac: 33
armorclass:
  - name: "AC"
    desc: "33; __Fort__: +22; __Ref__: +24; __Will__: +25"
hp: 260
health:
  - name: "HP"
    desc: "260; __Immunities__ fire; __Weaknesses__ cold 10, water 10"
abilities_mid:
  - name: "Solar Flare"
    desc: "(aura, divine, visual) 30 feet. When a creature ends its turn in the aura, it takes 2d6 fire damage (DC 33 basic Fortitude save). On a failed save, it also becomes dazzled until the end of its next turn. The anguished flame can activate or deactivate this aura by using a single action with the concentrate trait."
  - name: "Vulnerable to Blasphemy"
    desc: "If a creature the anguished flame can see and hear spends 1 action with the linguistic trait blaspheming against the gods, the anguished flame becomes sickened 1 until they Collect a Prayer from that creature."
speed: "30 feet, fly 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ flaming wing +25 (Agile, fire) __Damage__ 3d10+11 fire"
  - name: "Ranged"
    desc: "⬻ shining ray +27 (Fire, light, range increment 60 feet) __Damage__ 3d6+6 fire plus 3d6 spirit"
abilities_bot:
  - name: "Collect Prayer"
    desc: "⬺ (Emotion, mental) The anguished flame compels a creature they can see within 60 feet, who must attempt a DC 30 Will save."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature immediately uses its reaction to pray."
  - name: "Failure"
    desc: "The creature prays. It is slowed 1 and can't use reactions for 1 minute."
  - name: "Critical Failure"
    desc: "As failure, but the creature is slowed 2."
  - name: "Focus Gaze"
    desc: "⬻ (Concentrate, divine, visual)"
  - name: "Requirements"
    desc: "The anguished flame's solar flare aura is active"
  - name: "Effect"
    desc: "The anguished flame fixes their fiery eyes on a creature they can see within 30 feet. The target must immediately attempt a Fortitude save against the anguished flame's solar flare. If the creature was already dazzled by solar flare before attempting its save, a failed save causes it to become blinded until the end of its next turn. Ages In Darkness Over the eon of Lord Atreia's imprisonment inside the Garnet Brand, temples to the Lambent King lay dormant and decaying across the Plane of Fire, and within those temples, his children, known as ygnaires, began to fade. Without the light of their Lord of Fire, these elementals who waned became known as anguished flames. They eventually turned to unmoving bronze, frozen until Atreia's light shone down on them again."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 30, attack +22 - __Cantrips (7th)__ Detect Magic, Ignition, Light - __7th__ Fireball (×2), Interplanar Teleport - __Constant (5th)__ Truespeech"
sourcebook: "_Monster Core 2_, page 30."
```

```encounter-table
name: Anguished Flame
creatures:
  - 1: Anguished Flame
```
