---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Lovelorn"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/tiny
statblock: inline
name: "Lovelorn"
level: 4
source: "Monster Core 2"
aon_id: "creature-4469"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4469"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Lovelorn"
level: "Creature 4"
size: "Tiny"
trait_01: "Uncommon"
trait_02: "Undead"
trait_03: "Unholy"
modifier: 10
perception:
  - name: "Perception"
    desc: "Perception +10; (12 to Sense Motive) darkvision, lifesense 30 feet"
languages: "Common; (can't speak any language)"
skills:
  - name: "Skills"
    desc: "Athletics +11, Occultism +8, Stealth +13"
abilityMods: [4, 5, 3, -2, 2, 3]
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +9; __Ref__: +13; __Will__: +12"
hp: 60
health:
  - name: "HP"
    desc: "60 (void healing); __Immunities__ bleed, death effects, disease, mental, paralyzed, poison, unconscious"
abilities_mid:
  - name: "Gloom Aura"
    desc: "(aura, emotion, illusion, mental, occult) 60 feet. A lovelorn's presence instills unease and turns the air cold, dark, and stale. Creatures within the aura take a –1 circumstance penalty to saving throws to resist emotion effects. If the lovelorn makes a place home for a week or more, that location can become suffused with this magic even outside the lovelorn's aura, lasting until the lovelorn leaves or is destroyed."
  - name: "Skitter Away"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature ends its movement in a space adjacent to the lovelorn"
  - name: "Effect"
    desc: "The lovelorn Strides or Climbs 10 feet away from the triggering creature. This movement doesn't trigger reactions."
speed: "25 feet, climb 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fangs +13 (Finesse) __Damage__ 1d6+6 piercing plus 1d6 persistent bleed and cynic's curse"
  - name: "Melee"
    desc: "⬻ gory tendril +13 (Agile, finesse) __Damage__ 1d4+6 bludgeoning plus Grab"
abilities_bot:
  - name: "Cynic's Curse"
    desc: "(Curse, emotion, mental, Occult) A creature who takes damage from a lovelorn's fangs Strike must attempt a DC 19 Will save as it grows morose and listless. If the creature would be affected by a _calm_ spell that spell attempts to counteract this curse instead of having its normal effect."
  - name: "Critical Success"
    desc: "The target is unaffected."
  - name: "Success"
    desc: "For 1 minute the target can't benefit from helpful emotion effects but can still be affected by harmful emotion effects."
  - name: "Failure"
    desc: "As success, plus the target is fatigued for the same duration. __ Critical Failure__ As failure, but the curse’s effects are permanent. Lovelorn Keepsakes While a lovelorn has little use for treasure and rarely collects or hoards it for monetary value, these passionate undead often collect mementos and trinkets, both from their own lives before becoming undead and from their victims since becoming a lovelorn. While many of these treasures possess little intrinsic value—paintings, diaries, handmade toys, and the like—it's not uncommon for lovelorns to fill their twisted nests with bejeweled rings, necklaces, antique combs, or gold and platinum lockets."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 21, attack +13 - __Cantrips (2nd)__ Figment, Telekinetic Hand - __2nd__ Fear (×3), Illusory Creature (at will), Illusory Object (at will), Invisibility"
  - name: "Rituals"
    desc: "DC 21 - __2nd__ Create Undead (doesn't require secondary casters)"
sourcebook: "_Monster Core 2_, page 217."
```

```encounter-table
name: Lovelorn
creatures:
  - 1: Lovelorn
```
