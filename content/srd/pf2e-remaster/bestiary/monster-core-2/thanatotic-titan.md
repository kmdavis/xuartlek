---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Thanatotic Titan"
tags:
  - pf2e/creature/level/22
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/titan
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Thanatotic Titan"
level: 22
source: "Monster Core 2"
aon_id: "creature-4582"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4582"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Thanatotic Titan"
level: "Creature 22"
size: "Gargantuan"
trait_01: "Humanoid"
trait_02: "Rare"
trait_03: "Titan"
modifier: 36
perception:
  - name: "Perception"
    desc: "Perception +36; darkvision, _truesight_"
languages: "Chthonian, Common, Empyrean; telepathy 100 feet (page 362)"
skills:
  - name: "Skills"
    desc: "Athletics +45, Crafting +41, Deception +36, Intimidation +38, Religion +38, Stealth +36"
abilityMods: [10, 4, 9, 8, 6, 8]
abilities_top:
  - name: "Items"
    desc: "_+2 greater resilient full plate_, _+3 greater striking halberd_"
ac: 46
armorclass:
  - name: "AC"
    desc: "46; __Fort__: +37; __Ref__: +34; __Will__: +35 +4 status to all saves vs. mental or divine"
hp: 540
health:
  - name: "HP"
    desc: "540; __Immunities__ death effects, disease"
abilities_mid:
  - name: "Impossible Stature"
    desc: "(aura, divine, illusion, mental) 100 feet. Titans warp perception and distance around them to seem even larger and more imposing. A creature that enters or begins its turn within the emanation must succeed at a DC 45 Will save or its movement toward the titan is movement over difficult terrain (greater difficult terrain on a critical failure) for 1 round."
  - name: "Reactive Strike"
    desc: "⬲ The titan can use their Reactive Strike when a creature within their reach uses a concentrate action, in additional to its normal trigger. They disrupt actions on any hit, not just a critical hit—including triggering concentrate actions."
speed: "40 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _halberd_ +42 (Magical, reach 40 feet, versatile S) __Damage__ 4d10+25 piercing"
  - name: "Melee"
    desc: "⬻ foot +39 (Agile, reach 30 feet) __Damage__ 4d8+20 bludgeoning"
  - name: "Ranged"
    desc: "⬻ void chunk +39 (Brutal, range increment 200 feet, void) __Damage__ 3d12+10 bludgeoning plus 2d10 void and void explosion"
abilities_bot:
  - name: "Divine Rituals"
    desc: "DC 45 - __5th__ Planar Servitor, Resurrect"
  - name: "Godslayer"
    desc: "⭓ (Divine)"
  - name: "Trigger"
    desc: "The titan damages a creature capable of using divine spells or abilities"
  - name: "Effect"
    desc: "The creature must attempt a DC 45 Will save."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature can't use divine spells or abilities for 1 round and is frightened 2. Only powerful non-divine magic, such as _manifestation_, can undo this effect."
  - name: "Failure"
    desc: "As success, but the duration is 1 minute."
  - name: "Critical Failure"
    desc: "As success, but the duration is unlimited."
  - name: "Titanic Charge"
    desc: "⬺ The titan Strides twice and makes a melee Strike. If the Strike hits, the titan can cast _earthquake_ centered on the target as a free action."
  - name: "Trample"
    desc: "⬽ Huge or smaller, foot, DC 45"
  - name: "Void Explosion"
    desc: "If the titan's void chunk Strike isn't a critical failure, the chunk explodes, dealing 10d6 void damage to all creatures in a 20-foot burst (DC 45 basic Reflex save)."
  - name: "Wide Cleave"
    desc: "⬺ The titan makes a melee weapon Strike against each foe within their reach. This counts as three attacks for the titan's multiple attack penalty, but the penalty doesn't increase until all attacks have been made."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 45 - __5th__ Sending - __6th__ Scrying (×3) - __7th__ Spell Riposte - __8th__ Dispel Magic (at will), Spiritual Epidemic (at will), Suggestion (at will) - __10th__ Falling Stars, Massacre - __Constant (10th)__ Truesight"
sourcebook: "_Monster Core 2_, page 320."
```

```encounter-table
name: Thanatotic Titan
creatures:
  - 1: Thanatotic Titan
```
