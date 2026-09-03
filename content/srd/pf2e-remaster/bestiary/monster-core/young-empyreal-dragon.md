---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Young Empyreal Dragon"
tags:
  - pf2e/creature/level/10
  - pf2e/creature/trait/divine
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/large
statblock: inline
name: "Young Empyreal Dragon"
level: 10
source: "Monster Core"
aon_id: "creature-2941"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2941"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Young Empyreal Dragon"
level: "Creature 10"
size: "Large"
trait_01: "Divine"
trait_02: "Dragon"
trait_03: "Holy"
modifier: 21
perception:
  - name: "Perception"
    desc: "Perception +21; darkvision, lifesense (imprecise) 30 feet, scent (imprecise) 60 feet"
languages: "Common, Draconic, Empyrean; _truespeech_"
skills:
  - name: "Skills"
    desc: "Acrobatics +19, Athletics +22, Diplomacy +20, Heaven Lore +21, Intimidation +20, Medicine +21, Religion +21, Society +19"
abilityMods: [6, 3, 4, 3, 5, 4]
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +18; __Ref__: +19; __Will__: +21 +2 status to all saves vs. divine"
hp: 170
health:
  - name: "HP"
    desc: "170; __Immunities__ fear, paralyzed, sleep; __Weaknesses__ unholy 10"
abilities_mid:
  - name: "Inspiring Presence"
    desc: "(aura, emotion, mental) 20 feet. The mere sight of an empyreal dragon motivates other creatures. Creatures within the aura gain a +1 status bonus to saving throws and skill checks. The empyreal dragon can't gain the benefit of their own aura or other actions that use the aura, and they can choose to exclude any creatures from any benefit of the aura or action that uses the aura."
  - name: "Divine Deflection"
    desc: "⬲"
  - name: "Trigger"
    desc: "The dragon is critically hit by an attack"
  - name: "Effect"
    desc: "Divine power intercedes, preventing some of the damage. The dragon gains resistance 10 to all damage against the triggering attack."
speed: "60 feet, fly 150 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +22 (Holy, Magical, reach 10 feet) __Damage__ 2d10+9 piercing plus 1d8 spirit"
  - name: "Melee"
    desc: "⬻ claws +22 (Agile, Holy, Magical) __Damage__ 2d8+9 slashing plus 1d8 spirit"
  - name: "Melee"
    desc: "⬻ tail +20 (Holy, Magical, reach 15 feet) __Damage__ 2d10+9 bludgeoning plus 1d8 spirit"
  - name: "Melee"
    desc: "⬻ wing +20 (Agile, Magical, reach 10 feet) __Damage__ 1d10+9 slashing plus 1d8 spirit"
abilities_bot:
  - name: "Direct Halo"
    desc: "⬻ (Concentrate, Divine, Manipulate) The dragon tosses their halo to a square within 90 feet. While the halo is deployed in this way, the dragon loses their inspiring presence aura, and the aura instead emanates from the halo with the same emanation radius. The dragon can Sustain to recall the halo from any distance. The halo is made of pure light—it doesn't occupy space and can't be targeted or destroyed in any way."
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw Strikes and one wing Strike in any order."
  - name: "Draconic Momentum"
    desc: "The dragon recharges their Spirit Breath whenever they score a critical hit with a Strike."
  - name: "Halo Pulse"
    desc: "⬺ (Concentrate, Divine) The dragon chooses one effect to impose on creatures in their inspiring presence aura. The dragon can't use Halo Pulse again for 1d4 rounds."
  - name: "Repulsion"
    desc: "Each creature must succeed at a DC 29 Fortitude save or be pushed until it's no longer in the aura."
  - name: "Restoration"
    desc: "(healing, vitality) Each creature recovers 5d8 Hit Points."
  - name: "Spirit Breath"
    desc: "⬺ (Divine, Holy, Spirit) The dragon unleashes a blast of holy fire that deals 9d8 spirit damage in a 40-foot cone (DC 29 basic Reflex save). The dragon can't use Spirit Breath again for 1d4 rounds."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 29, attack +21 - __3rd__ Holy Light (at will) - __5th__ Heal - __Constant (5th)__ Truespeech"
sourcebook: "_Monster Core_, page 114."
```

```encounter-table
name: Young Empyreal Dragon
creatures:
  - 1: Young Empyreal Dragon
```
