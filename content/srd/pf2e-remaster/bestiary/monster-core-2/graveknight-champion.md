---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Graveknight Champion"
tags:
  - pf2e/creature/level/15
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Graveknight Champion"
level: 15
source: "Monster Core 2"
aon_id: "creature-4420"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4420"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Graveknight Champion"
level: "Creature 15"
size: "Medium"
trait_01: "Uncommon"
trait_02: "Undead"
trait_03: "Unholy"
modifier: 27
perception:
  - name: "Perception"
    desc: "Perception +27; darkvision"
languages: "Common, Necril"
skills:
  - name: "Skills"
    desc: "Athletics +31, Deity Lore +27, Intimidation +29, Religion +27"
abilityMods: [8, 4, 5, 2, 4, 6]
abilities_top:
  - name: "Items"
    desc: "Composite Shortbow (20 arrows), _+2 resilient full plate_, Greatpick"
ac: 38
armorclass:
  - name: "AC"
    desc: "38; __Fort__: +28; __Ref__: +26; __Will__: +25"
hp: 275
health:
  - name: "HP"
    desc: "275 (rejuvenation, void healing); __Immunities__ bleed, death, disease, fire, paralyzed, poison, unconscious"
abilities_mid:
  - name: "Clutching Armor"
    desc: "⬲ (arcane)"
  - name: "Trigger"
    desc: "A creature attempts to move away from the graveknight champion"
  - name: "Effect"
    desc: "The graveknight champion's armor animates and attempts to Grab the triggering creature. It makes an Athletics check to Grapple at +29. The armor can continue to Grapple the creature normally. Since the armor is grappling the creature, the graveknight doesn't need a free hand to do so."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _greatpick_ +30 (fatal d12, fire, magical) __Damage__ 3d10+16 slashing plus 1d6 fire"
  - name: "Melee"
    desc: "⬻ fist +30 (Agile, fire, magical) __Damage__ 3d6+16 bludgeoning plus 1d6 fire"
  - name: "Ranged"
    desc: "⬻ _composite shortbow_ +28 (deadly d10, fire, magical, range increment 60 feet, reload 0) __Damage__ 3d6+10 piercing plus 1d6 fire"
abilities_bot:
  - name: "Innate Divine Spells"
    desc: "DC 33, attack +25 - __Cantrips (7th)__ Divine Lance, Light, Shield, Void Warp - __4th__ Fireball - __5th__ Chilling Darkness, Divine Immolation - __6th__ Fireball, Spiritual Armament - __7th__ Eclipse Burst, Execute"
  - name: "Channel Magic"
    desc: "⬺ The graveknight champion redirects magical energies through its armor, allowing it to deliver magic through an attack. The graveknight champion Casts a Spell that takes 1 or 2 actions to cast and requires a spell attack modifier. The effects of the spell don't occur immediately but are imbued into an attack instead. The graveknight champion then makes a melee Strike with a weapon or unarmed attack. The spell is coupled with the attack, using the attack roll result to determine the effects of both the Strike and the spell. This counts as two attacks for the graveknight's multiple attack penalty but doesn't apply the penalty until after they've completed Channeling Magic. The graveknight champion can't use Channel Magic again for 1d4 rounds."
  - name: "Devastating Blast"
    desc: "⬺ (Arcane, fire) The graveknight champion unleashes a 30-foot cone of energy. Creatures in the area take 9d12 fire with a DC 36 basic Reflex save. The graveknight champion can use this ability once every 1d4 rounds."
  - name: "Graveknight's Curse"
    desc: "(Arcane, curse) This curse affects anyone who wears a graveknight champion's armor for at least 1 hour"
  - name: "Saving Throw"
    desc: "DC 40 Will save"
  - name: "Onset"
    desc: "1 hour"
  - name: "Stage 1"
    desc: "doomed 1 and can't remove armor (1 day)"
  - name: "Stage 2"
    desc: "doomed 2, –10- foot status penalty to Speeds, and can't remove armor (1 day)"
  - name: "Stage 3"
    desc: "dies and transforms into the armor's graveknight."
  - name: "Ruinous Weapons"
    desc: "Any weapon or unarmed attack the graveknight uses gains the effects of a _+1 greater striking weapon_ and a _greater flaming_ weapon rune."
  - name: "Weapon Master"
    desc: "The graveknight has access to the critical specialization effects of any weapons they wield."
sourcebook: "_Monster Core 2_, page 173."
```

```encounter-table
name: Graveknight Champion
creatures:
  - 1: Graveknight Champion
```
