---
obsidianUIMode: preview
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
aon_id: "creature-3510"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3510"
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
    desc: "Perception +13"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +17, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +15, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +15, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +17, [[srd/pf2e/compendium/rules-elements/skills/lore|Patron Lore]] +15"
abilityMods: [0, 4, 1, 4, 2, 2]
abilities_top:
  - name: "Firearm Familiar"
    desc: "The gunwitch's firearm acts as their familiar but remains a mindless item with no actions. The master abilities it grants are included in the stat block."
  - name: "Items"
    desc: "[[srd/pf2e/compendium/equipment/staves/musket-staff-of-force|_musket staff of force_]] (20 rounds)"
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
    desc: "⬻ _musket staff_ +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/two-hand|two-hand d6]]) __Damage__ 1d4+6 bludgeoning plus 1d6 force"
  - name: "Melee"
    desc: "⬻ fist +15 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/nonlethal|Nonlethal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d4+6 bludgeoning"
  - name: "Ranged"
    desc: "⬻ _musket staff_ +18 ([[srd/pf2e/compendium/rules-elements/traits/npc-core/concussive|Concussive]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fatal|fatal d10]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], range increment 70 feet, reload 1) __Damage__ 1d6+6 piercing plus 1d6 force"
abilities_bot:
  - name: "Witch Hex Spells"
    desc: "DC 25, 1 Focus Point - __Cantrips (4th)__ [[srd/pf2e/compendium/spells/cantrips/nudge-fate|Nudge Fate]] - __4th__ [[srd/pf2e/compendium/spells/focus/needle-of-vengeance|Needle of Vengeance]]"
  - name: "Bewitched Shot"
    desc: "⬺"
  - name: "Requirements"
    desc: "The gunwitch is wielding their firearm familiar and has a hex bullet loaded in it (see Hex Bullet)"
  - name: "Effect"
    desc: "The gunwitch Casts a Spell that takes 1 or 2 actions to cast into their bullet, then Strikes with their firearm familiar, shooting the magic bullet. This counts as two attacks for the gunwitch's multiple attack penalty. On a hit, the target is also affected by the spell, though the target gets any normal defenses allowed by the spell. If the spell is targeted, it targets the creature that was hit and no one else. If the spell is an area, the target must be in the area. A burst is centered on a corner of the target's square if the target is Medium or smaller or the corner of a square closest to the creature's center if it's Large or larger. A cone or line emits from a square of the gunwitch's choice adjacent to the target."
  - name: "Bullet Storm"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|Occult]])"
  - name: "Requirements"
    desc: "The gunwitch is wielding their firearm familiar and has a hex bullet loaded into it (see Hex Bullet)"
  - name: "Effect"
    desc: "The gunwitch unleashes a flurry of projectiles. Each creature in a 60-foot emanation takes 8d6 piercing damage with a DC 25 basic Reflex save."
  - name: "Hex Bullet"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|Occult]])"
  - name: "Frequency"
    desc: "once per round"
  - name: "Effect"
    desc: "The gunwitch conjures a magical hex bullet in their firearm. It can be used as a normal bullet or for the Bewitched Shot and Bullet Storm abilities. The bullet vanishes if not fired by the end of the turn."
  - name: "Recall Firearm"
    desc: "⬽ ([[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/occult|Occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/teleportation|Teleportation]])"
  - name: "Frequency"
    desc: "once per day"
  - name: "Requirement"
    desc: "The gunwitch's firearm familiar is within 1 mile"
  - name: "Effect"
    desc: "The gunwitch summons their firearm into their hand or hands. The Code Most mavericks adhere to a code of conduct, often one that's in direct opposition to the norms of society. This can make them outsiders or rebels, but it also allows them to be true to themselves and follow their own path, rather than conforming to expectations or rules imposed on them by others."
spellcasting:
  - name: "Occult Prepared Spells"
    desc: "DC 25, attack +17 - __Cantrips (4th)__ [[srd/pf2e/compendium/spells/cantrips/daze|Daze]], [[srd/pf2e/compendium/spells/cantrips/detect-magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/light|Light]], [[srd/pf2e/compendium/spells/cantrips/read-aura|Read Aura]], [[srd/pf2e/compendium/spells/cantrips/telekinetic-projectile|Telekinetic Projectile]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/enfeeble|Enfeeble]] (×2), [[srd/pf2e/compendium/spells/rank-1/sure-strike|Sure Strike]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/invisibility|Invisibility]], [[srd/pf2e/compendium/spells/rank-2/telekinetic-maneuver|Telekinetic Maneuver]] (×2) - __3rd__ [[srd/pf2e/compendium/spells/rank-3/haste|Haste]], [[srd/pf2e/compendium/spells/rank-3/paralyze|Paralyze]], [[srd/pf2e/compendium/spells/rank-3/slow|Slow]] - __4th__ [[srd/pf2e/compendium/spells/rank-4/confusion|Confusion]], [[srd/pf2e/compendium/spells/rank-4/flicker|Flicker]], [[srd/pf2e/compendium/spells/rank-1/phantom-pain|Phantom Pain]]"
sourcebook: "_NPC Core_, page 78."
```

```encounter-table
name: Gunwitch
creatures:
  - 1: Gunwitch
```
