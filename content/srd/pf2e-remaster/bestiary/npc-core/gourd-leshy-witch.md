---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Gourd Leshy Witch"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/leshy
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/small
statblock: inline
name: "Gourd Leshy Witch"
level: 6
source: "NPC Core"
aon_id: "creature-3659"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3659"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Gourd Leshy Witch"
level: "Creature 6"
size: "Small"
trait_01: "Leshy"
trait_02: "Plant"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12; low-light vision"
languages: "Common, Fey; _speak with plants_ (gourds only)"
skills:
  - name: "Skills"
    desc: "Acrobatics +12, Intimidation +13, Nature +14, Occultism +16, Survival +12"
abilityMods: [2, 2, 1, 4, 2, 1]
abilities_top:
  - name: "Items"
    desc: "_+1 broom_ (functions as a staff), Dagger"
ac: 22
armorclass:
  - name: "AC"
    desc: "22; __Fort__: +11; __Ref__: +14; __Will__: +14"
hp: 80
health:
  - name: "HP"
    desc: "80"
abilities_mid:
  - name: "Verdant Burst"
    desc: "(healing, primal, vitality) When the gourd leshy witch dies, a burst of primal energy explodes from their body, restoring 4d8 Hit Points to each plant creature in a 30-foot emanation. This area immediately sprouts gourds, becoming difficult terrain. If the terrain is not a viable environment for these plants, they wither after 24 hours."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _broom_ +13 (Magical, two-hand 1d8) __Damage__ 1d4+6 bludgeoning plus 1d6 void"
  - name: "Melee"
    desc: "⬻ dagger +12 (Agile, Finesse, versatile S) __Damage__ 1d4+6 piercing plus 1d6 void"
  - name: "Melee"
    desc: "⬻ fist +12 (Agile, Finesse, Nonlethal, Unarmed) __Damage__ 1d4+6 bludgeoning plus 1d6 void"
  - name: "Ranged"
    desc: "⬻ dagger +12 (Agile, Finesse, thrown 10 feet, versatile S) __Damage__ 1d4+6 piercing plus 1d6 void"
abilities_bot:
  - name: "Witch Hex Spells"
    desc: "DC 24, 1 Focus Point - __3rd__ Wilding Word"
  - name: "Change Shape"
    desc: "⬻ (Concentrate, Polymorph, primal The gourd leshy witch transforms into a Small gourd. This ability otherwise uses the effects of _one with plants_.)"
  - name: "Short Flight"
    desc: "(Concentrate, Occult)"
  - name: "Frequency"
    desc: "once per round"
  - name: "Requirements"
    desc: "The gourd leshy witch is wielding a broom"
  - name: "Effect"
    desc: "The gourd leshy hops on their broom, which briefly takes flight. The witch Flies 20 feet (or 40 feet if they spend 2 actions), though they must end this movement on solid ground or fall at the end of their turn."
  - name: "Sweeping Spell"
    desc: "⬻ (Manipulate, Occult, Spellshape)"
  - name: "Requirements"
    desc: "The gourd leshy witch is wielding their broom"
  - name: "Effect"
    desc: "If the next action the gourd leshy witch uses is to cast a non-cantrip spell that deals damage to a single target, the witch's broom flies out and attempts to Shove that creature with an Athletics modifier of +16. On a critical success, the target is also knocked prone. The broom immediately returns to the gourd leshy witch's hand."
spellcasting:
  - name: "Occult Prepared Spells"
    desc: "DC 24, attack +16 - __Cantrips (3rd)__ Daze, Detect Magic, Figment, Shield, Void Warp - __1st__ Fear (×2), Ill Omen - __2nd__ Force Barrage, Grim Tendrils, Paranoia - __3rd__ Force Barrage, Slow, Vampiric Feast"
  - name: "Primal Innate Spells"
    desc: "DC 24 - __Constant (3rd)__ Speak with Plants (gourds only)"
sourcebook: "_NPC Core_, page 202."
```

```encounter-table
name: Gourd Leshy Witch
creatures:
  - 1: Gourd Leshy Witch
```
