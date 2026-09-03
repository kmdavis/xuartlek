---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Adult Resurrection Dragon"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/divine
  - pf2e/creature/trait/dragon
  - pf2e/creature/trait/large
statblock: inline
name: "Adult Resurrection Dragon"
level: 12
source: "Monster Core 2"
aon_id: "creature-4361"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4361"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Adult Resurrection Dragon"
level: "Creature 12"
size: "Large"
trait_01: "Divine"
trait_02: "Dragon"
modifier: 25
perception:
  - name: "Perception"
    desc: "Perception +25; darkvision, scent (imprecise) 60 feet"
languages: "Common, Draconic, Necril"
skills:
  - name: "Skills"
    desc: "Acrobatics +20, Arcana +22, Athletics +25, Diplomacy +23, Medicine +25, Necromancy Lore +26, Religion +25, Stealth +22"
abilityMods: [7, 4, 5, 4, 7, 5]
ac: 32
armorclass:
  - name: "AC"
    desc: "32; __Fort__: +21; __Ref__: +20; __Will__: +25"
hp: 230
health:
  - name: "HP"
    desc: "230; __Immunities__ death effects, paralyzed, sleep; __Resistances__ spirit 15"
abilities_mid:
  - name: "Risen Commander"
    desc: "(divine) A resurrection dragon has a strong connection with its minions and can Sustain _summon undead_ or _invoke spirits_ as a free action once per turn. __Reawaken!__ ⬲ (divine, spirit, vitality)"
  - name: "Trigger"
    desc: "A living creature the resurrection dragon can see dies"
  - name: "Effect"
    desc: "The resurrection dragon uses divine and vital energy to retether the soul to its dead body. The willing creature is returned to life stabilized at 0 HP. A creature can be resurrected by this ability only once."
  - name: "Siphon Life"
    desc: "⬲ (divine, healing, vitality)"
  - name: "Trigger"
    desc: "A creature within 60 feet uses a healing effect that restores Hit Points"
  - name: "Effect"
    desc: "The resurrection dragon redirects vital energies away from the effect, minimizing its impact. The triggering effect results in the minimum amount on any dice rolls to restore Hit Points, and any flat values for restoring Hit Points (such as the additional Hit Points for a two-action _heal_ spell) are cut in half. The dragon then gains 2d8 temporary Hit Points that last for 1 round."
speed: "40 feet, fly 160 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +26 (Magical, reach 10 feet) __Damage__ 3d10+11 piercing plus 1d6 void"
  - name: "Melee"
    desc: "⬻ claw +26 (Agile, magical) __Damage__ 3d8+11 slashing"
  - name: "Melee"
    desc: "⬻ tail +24 (Magical, reach 15 feet) __Damage__ 3d10+11 bludgeoning"
abilities_bot:
  - name: "Draconic Frenzy"
    desc: "⬺ The dragon makes two claw strikes and one tail strike in any order."
  - name: "Draconic Momentum"
    desc: "The dragon recharges their Soul Siphoning Breath whenever they score a critical hit with a Strike."
  - name: "Soul Siphoning Breath"
    desc: "⬺ (Divine, void) The dragon unleashes a torrent of divine energy, dealing 11d6 void damage in a 40-foot cone (DC 32 basic Fortitude save) that draws the life force from creatures within. The dragon gains fast healing 10 until their Soul Siphoning Breath recharges. The resurrection dragon can't use Soul Siphoning Breath again for 1d4 rounds."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 32 - __Cantrips (6th)__ Guidance, Stabilize, Void Warp - __4th__ Talking Corpse (at will) - __5th__ Invoke Spirits (×2) - __6th__ Harm (×2), Raise Dead, Summon Undead (at will) __Arise!__ (Divine, exploration, healing) The resurrection dragon uses their mastery over life energy to cast their own soul into the Boneyard and pull a willing creature's soul back to its body in a process that takes 1 hour. This has the effects of _raise dead_, except the maximum level of the target is 8th and the soul is tethered to the dragon's. Only one creature can be tethered to the dragon's soul at a time. If the creature and the dragon are no longer on the same plane or the dragon dies, the raised creature dies and can't be raised with Arise! again. The dragon can Dismiss the connection at any time. Doing so doesn't prevent the dragon from raising the creature with Arise! again. While raised in this way, the creature is still a valid target for _raise dead_, _resurrection_, and similar effects. Returning the creature to life in this way fully restores the creature, severing the connection to the dragon and allowing the dragon to establish a connection with a different creature."
sourcebook: "_Monster Core 2_, page 129."
```

```encounter-table
name: Adult Resurrection Dragon
creatures:
  - 1: Adult Resurrection Dragon
```
