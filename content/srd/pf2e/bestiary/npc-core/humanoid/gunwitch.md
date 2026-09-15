---
noteType: pf2eMonster
aliases: "Gunwitch"
tags:
  - pf2e/creature/level/7
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/medium
statblock: inline
name: "Gunwitch"
level: 7
source: "NPC Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3510"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Gunwitch"
level: "Creature 7"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Rare"
modifier: 13
perception:
  - name: "Perception"
    desc: "+13"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +17, [[srd/pf2e/compendium/rules-elements/skills/Crafting|Crafting]] +15, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +15, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +17, [[srd/pf2e/compendium/rules-elements/skills/Lore|Patron Lore]] +15"
abilityMods: [0, 4, 1, 4, 2, 2]
abilities_top:
  - name: "Firearm Familiar"
    desc: "The gunwitch's firearm acts as their familiar but remains a mindless item with no actions. The master abilities it grants are included in the stat block."
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/staves/Musket Staff of Force|_musket staff of force_]] (20 rounds)"
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +12; __Ref__: +15; __Will__: +15"
hp: 90
health:
  - name: "HP"
    desc: "90"
abilities_mid:
  - name: "Acrobatic Dodge"
    desc: "⬲"
  - name: "Trigger"
    desc: "An attacker the gunwitch can observe targets them with an attack"
  - name: "Effect"
    desc: "The gunwitch gains a +2 circumstance bonus to AC against the triggering attack, and after the attack the gunwitch [[srd/pf2e/compendium/rules-elements/actions/player-core#Leap|Leaps]]."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _musket staff_ +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Two-Hand|two-hand d6]]) __Damage__ 1d4+6 bludgeoning plus 1d6 force"
  - name: "Melee"
    desc: "⬻ fist +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unarmed|Unarmed]]) __Damage__ 1d4+6 bludgeoning"
  - name: "Ranged"
    desc: "⬻ _musket staff_ +18 ([[srd/pf2e/compendium/rules-elements/traits/npc-core/Concussive|Concussive]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Fatal|fatal d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], range increment 70 feet, reload 1) __Damage__ 1d6+6 piercing plus 1d6 force"
abilities_bot:
  - name: "Witch Hex Spells"
    desc: "DC 25, 1 Focus Point - __Cantrips (4th)__ [[srd/pf2e/compendium/spells/cantrips/Nudge Fate|Nudge Fate]] - __4th__ [[srd/pf2e/compendium/spells/focus/Needle of Vengeance|Needle of Vengeance]]"
  - name: "Bewitched Shot"
    desc: "⬺"
  - name: "Requirements"
    desc: "The gunwitch is wielding their firearm familiar and has a hex bullet loaded in it (see Hex Bullet)"
  - name: "Effect"
    desc: "The gunwitch Casts a Spell that takes 1 or 2 actions to cast into their bullet, then Strikes with their firearm familiar, shooting the magic bullet. This counts as two attacks for the gunwitch's multiple attack penalty. On a hit, the target is also affected by the spell, though the target gets any normal defenses allowed by the spell. If the spell is targeted, it targets the creature that was hit and no one else. If the spell is an area, the target must be in the area. A burst is centered on a corner of the target's square if the target is Medium or smaller or the corner of a square closest to the creature's center if it's Large or larger. A cone or line emits from a square of the gunwitch's choice adjacent to the target."
  - name: "Bullet Storm"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|Occult]])"
  - name: "Requirements"
    desc: "The gunwitch is wielding their firearm familiar and has a hex bullet loaded into it (see Hex Bullet)"
  - name: "Effect"
    desc: "The gunwitch unleashes a flurry of projectiles. Each creature in a 60-foot emanation takes 8d6 piercing damage with a DC 25 basic Reflex save."
  - name: "Hex Bullet"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|Occult]])"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The gunwitch conjures a magical hex bullet in their firearm. It can be used as a normal bullet or for the Bewitched Shot and Bullet Storm abilities. The bullet vanishes if not fired by the end of the turn."
  - name: "Recall Firearm"
    desc: "⬽ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|Occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Teleportation|Teleportation]])"
  - name: "Frequency"
    desc: "once per day"
  - name: "Requirement"
    desc: "The gunwitch's firearm familiar is within 1 mile"
  - name: "Effect"
    desc: "The gunwitch summons their firearm into their hand or hands. The Code Most mavericks adhere to a code of conduct, often one that's in direct opposition to the norms of society. This can make them outsiders or rebels, but it also allows them to be true to themselves and follow their own path, rather than conforming to expectations or rules imposed on them by others."
spellcasting:
  - name: "Occult Prepared Spells"
    desc: "DC 25, attack +17 - __Cantrips (4th)__ [[srd/pf2e/compendium/spells/cantrips/Daze|Daze]], [[srd/pf2e/compendium/spells/cantrips/Detect Magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/Light|Light]], [[srd/pf2e/compendium/spells/cantrips/Read Aura|Read Aura]], [[srd/pf2e/compendium/spells/cantrips/Telekinetic Projectile|Telekinetic Projectile]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Enfeeble|Enfeeble]] (×2), [[srd/pf2e/compendium/spells/rank-1/Sure Strike|Sure Strike]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Invisibility|Invisibility]], [[srd/pf2e/compendium/spells/rank-2/Telekinetic Maneuver|Telekinetic Maneuver]] (×2) - __3rd__ [[srd/pf2e/compendium/spells/rank-3/Haste|Haste]], [[srd/pf2e/compendium/spells/rank-3/Paralyze|Paralyze]], [[srd/pf2e/compendium/spells/rank-3/Slow|Slow]] - __4th__ [[srd/pf2e/compendium/spells/rank-4/Confusion|Confusion]], [[srd/pf2e/compendium/spells/rank-4/Flicker|Flicker]], [[srd/pf2e/compendium/spells/rank-1/Phantom Pain|Phantom Pain]]"
sourcebook: "_NPC Core_, page 78."
```

```encounter-table
name: Gunwitch
creatures:
  - 1: Gunwitch
```
