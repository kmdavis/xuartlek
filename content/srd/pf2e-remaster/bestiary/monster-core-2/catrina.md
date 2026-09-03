---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Catrina"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/monitor
  - pf2e/creature/trait/psychopomp
  - pf2e/creature/trait/medium
statblock: inline
name: "Catrina"
level: 5
source: "Monster Core 2"
aon_id: "creature-4522"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4522"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Catrina"
level: "Creature 5"
size: "Medium"
trait_01: "Monitor"
trait_02: "Psychopomp"
modifier: 13
perception:
  - name: "Perception"
    desc: "Perception +13; darkvision, lifesense 60 feet"
languages: "Chthonian, Diabolic, Empyrean, Requian; telepathy 120 feet, _truespeech_"
skills:
  - name: "Skills"
    desc: "Acrobatics +14, Boneyard Lore +11, Diplomacy +14, Intimidation +14, Medicine +12, Occultism +11, Religion +12"
abilityMods: [0, 5, 4, 2, 4, 5]
ac: 22
armorclass:
  - name: "AC"
    desc: "22; __Fort__: +11; __Ref__: +12; __Will__: +13 +1 status to all saves vs. magic"
hp: 75
health:
  - name: "HP"
    desc: "75; __Immunities__ death effects, disease; __Resistances__ poison 5, void 5"
abilities_mid:
  - name: "Calming Presence"
    desc: "(aura, divine, emotion, incapacitation) 30 feet. A creature that begins its turn within the area must attempt a DC 18 Will save."
  - name: "Critical Success"
    desc: "The creature is unaffected and is temporarily immune to calming presence for 24 hours."
  - name: "Success"
    desc: "The creature's attack rolls take a –1 status penalty for 1 round."
  - name: "Failure"
    desc: "Any emotion effects that would affect the creature are suppressed, and the creature can't use hostile actions. If the creature is subjected to hostility from any other creature, it ceases to be affected by calming presence and is temporarily immune to calming presence for 24 hours."
  - name: "Critical Failure"
    desc: "As failure, but hostility doesn't end the effect."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +14 (Agile, Finesse) __Damage__ 2d8+2 bludgeoning plus shepherd's touch"
abilities_bot:
  - name: "Compel Condemned"
    desc: "⬻ (Divine, Incapacitation, Mental) The catrina telepathically compels a creature within 30 feet to approach and allow the catrina to kiss them, in preparation for using Kiss of Death. The target must attempt a DC 22 Will save."
  - name: "Success"
    desc: "The creature is unaffected and is temporarily immune to Compel Condemned for 24 hours."
  - name: "Failure"
    desc: "The creature must spend each of its actions to move closer to the catrina as quickly as possible while avoiding obvious dangers. If the compelled creature is adjacent to the catrina, it stays still and doesn't act. If the creature takes any damage, the effect ends and the creature is temporarily immune to Compel Condemned for 24 hours. This effect lasts for 1 round, but if the catrina uses this ability again on subsequent rounds, it extend the duration by 1 round for all affected creatures."
  - name: "Critical Failure"
    desc: "As failure, but damage does not end the effect."
  - name: "Kiss of Death"
    desc: "⬺ (Death, Divine, Manipulate, Void) The catrina gives a long, passionate kiss to an unconscious or willing creature, dealing 3d6 void damage. Any creature damaged by the same catrina's Kiss of Death for 3 consecutive rounds becomes unconscious and is dying 1."
  - name: "Shepherd's Touch"
    desc: "A psychopomp's Strikes affect incorporeal creatures with the effects of a _ghost touch_ property rune and deal 1d6 void damage to living creatures and 1d6 vitality damage to undead. Dealing With Grief Death often comes with great emotional distress. While catrinas handle these feelings for souls in the afterlife, the emotions of the deceased's loved ones can become a complication. In most cases, a different type of psychopomp—calacas—will handle the matter in the mortal Universe. Similar to catrinas in appearance, these skeletal psychopomps make use of song to ease the feelings of mortals. In extreme cases, such as the threat of a loved one pursuing vile necromancy to restore the dead, a catrina can establish a brief communication between the dead and their loved ones."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 22 - __Cantrips (3rd)__ Light - __2nd__ Invisibility (at will; self only) - __3rd__ Illusory Disguise - __4th__ Talking Corpse (at will), Translocate - __Constant (5th)__ Truespeech"
sourcebook: "_Monster Core 2_, page 263."
```

```encounter-table
name: Catrina
creatures:
  - 1: Catrina
```
