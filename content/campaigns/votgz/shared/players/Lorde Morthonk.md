---
hp: "24"
ac: "18"
modifier: "6"
level: "2"
player: Joel
class: Necromancer
ancestry: Awakened Animal
source: Foundry export fvtt-Actor-lorde-morthonk-(joel)-WjgtBBaXatZRzBIC.json
publish: true
visibility: players
type: pc
---

![[Lorde Morthonk Portrait.webp|portrait]]
![[Lorde Morthonk Token.webp|token]]

```statblock
layout: Basic Pathfinder 2e Layout
name: Lorde Morthonk
level: 2
ancestry: Awakened Animal # unrendered
heritage: Flying Animal # unrendered
background: Cursed # unrendered
class: Necromancer # unrendered

rare_03: Necromancer # class
rare_04: Cursed # background
size: Small
trait_01: Awakened Animal
trait_02: Beast

modifier: 6 # unrendered
perception:
  - name: Perception
    desc: "+6"
languages:
- [[srd/pf2e/compendium/rules-elements/languages#Common|Common]]
- [[srd/pf2e/compendium/rules-elements/languages#Necril|Necril]]
- [[srd/pf2e/compendium/rules-elements/languages#Thalassic|Thalassic]]
- [[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]]
- Requian
skills:
  acrobatics: +6
  arcana: +8
  intimidation: +4
  medicine: +6
  nature: +6
  occultism: +8
  religion: +6
  survival: +6
  undead_lore_lore: +8
  curse_lore_lore: +8
abilityMods: [0,2,1,4,2,0]

ac: 18 # unrendered
armorclass:
  - name: "AC"
    desc: "18; __Fort__: +7; __Ref__: +6; __Will__: +6"
hp: 24 # unrendered
health:
  - name: "HP"
    desc: 24
saves: # unrendered
  fortitude: +7
  reflex: +6
  will: +6

speed: 20 feet
attacks:
  - name: "Melee"
    desc: "⬻ beak +6 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unarmed|Unarmed]]) __Damage__ 1d6 piercing"
```

## Feats and Features

### Class Features

[[srd/pf2e/compendium/character/class-features/necromancer/Fatal Method|**Fatal Method**]] *Level 1*

`necromancer`

As a necromancer, you select one fatal method at 1st level. This choice determines your combat style: a puppeteer who creates more thralls to fuel spells, or a reaper who becomes more combat-focused with weapons and armor.

- Puppeteer

- Reaper

[[srd/pf2e/compendium/character/class-features/necromancer/Grave Spells|**Grave Spells**]] *Level 1*

`necromancer`

Your necromantic prowess allows you to create unique effects called grave spells, which are a type of focus spell. It costs 1 Focus Point to cast a focus spell. You refill your focus pool during your daily preparations, and you can regain 1 Focus Point by spending 10 minutes using the Refocus activity to speak to the dead, meditate on local supernatural activity, or contemplate anatomical truths. If you have a thrall when you begin Refocusing, you can destroy it to regain 2 Focus Points when you Refocus.

Focus spells are automatically heightened to half your level rounded up, much like cantrips. Focus spells don't require spell slots, and you can't cast them using spell slots. The maximum Focus Points your focus pool can hold is equal to the number of focus spells you have, but can never be more than 3 points.

You gain the Necrotic Bomb grave spell and an additional grave spell from your Grim Fascination at 1st level. Therefore, you start with a focus pool of 2 Focus Points. You can learn additional grave spells through necromancer feats.
Grave CantripsGrave cantrips are special grave spells that don't cost Focus Points, so you can use them as often as you like. Grave cantrips are granted in addition to the cantrips you choose with necromancer spellcasting. Unlike other cantrips, you can't swap out grave cantrips gained from necromancer feats at a later level, unless you swap out the specific feat via retraining. You learn the Create Thrall and Thrall Charge grave cantrips, which allow you to summon expendable thralls and manipulate them to do your bidding.

[[srd/pf2e/compendium/character/class-features/necromancer/Grim Fascination|**Grim Fascination**]] *Level 1*

`necromancer`

As a necromancer, you select one grim fascination at 1st level. This fascination is a focus of necrotic study that you have developed a greater mastery over. However, grim fascinations don't prevent you from studying and using other forms of necromancy. Your choice of grim fascination grants you a grave spell and a thrall enhancement that applies to any thrall you create.

- Blood

- Bone

- Flesh

- Spirit

[[srd/pf2e/compendium/character/class-features/necromancer/Mastery of Life and Death|**Mastery of Life and Death**]] *Level 1*

`necromancer`

You have studied the delicate balance of life and death to such a point that you can dance between them with ease. Whenever you Cast a Spell or use an ability that would deal void or vitality damage, you can choose for the spell to do either void or vitality damage to each target separately. When you Cast a Spell or use an ability that would affect or target only living creatures or only undead creatures, you can affect and target both. This does not apply to the healing effects of spells or abilities. For example, you could have the Harm spell deal vitality damage to undead enemies, but it would not be able to heal living allies.

[[srd/pf2e/compendium/character/class-features/necromancer/Necromancer Spellcasting|**Necromancer Spellcasting**]] *Level 1*

`necromancer`

Your studies into the nature of life and death have resulted in the ability to cast occult spells. You are a spellcaster, and you can cast spells of the occult tradition using the Cast a Spell activity. As a necromancer, your chants are generally inspired by laments, requiems, and other rites for the dead, while your gestures evoke the unnatural movement of muscle and cracking of bone.

At 1st level, you can prepare one 1st-rank spell and five cantrips each morning from your dirge (see below). Prepared spells remain available to you until you cast them or until you prepare your spells again. The number of spells you can prepare each day is called your spell slots.

As you increase in level as a necromancer, the number of spells you can prepare each day increases, as does the highest rank of spell you can cast, as shown in the Necromancer Spells per Day table.

Some of your spells require you to attempt a spell attack to see how effective they are or for your enemies to roll against your spell DC (typically by attempting a saving throw). Since your key attribute is Intelligence, your spell attack modifier and spell DC use your Intelligence modifier.
Heightening SpellsWhen you get spell slots of 2nd rank and higher, you can fill those slots with stronger versions of lower-rank spells. This increases the spell's rank, heightening it to match the spell slot. Many spells have specific improvements when they are heightened to certain ranks.
CantripsSome of your spells are cantrips. A cantrip is a special type of spell that doesn't use spell slots. You can cast a cantrip at will, any number of times per day. A cantrip is always automatically heightened to half your level rounded up--this is usually equal to the highest rank of necromancer spell slot you have. For example, as a 1st-level necromancer, your cantrips are 1st-rank spells, and as a 5th-level necromancer, your cantrips are 3rd-rank spells.
DirgeYour occult spells become a part of an internal dirge that echoes throughout your body, bones, and even your spirit. Each day, to prepare your spells, you pull forth pieces of your dirge to vocalize. Your dirge contains your choice of eight occult cantrips, the 1st-rank spell Harm, and four other 1st-rank occult spells of your choice. You choose these from the common spells on the occult spell list or from other occult spells you gain access to. You can prepare and cast *harm* as an occult spell.

Each time you gain a level, you add two occult spells to your dirge, of any spell rank for which you have spell slots, chosen from common occult spells or others you gain access to and learn via Learn a Spell.

[[srd/pf2e/compendium/character/Fatal Methods#Puppeteer|**Puppeteer**]] *Level 1*

`necromancer`

You prefer to study life and death from afar. You gain the Consume Thrall action and the thrall proliferation ability.

**Thrall Proliferation** Once per round when you cast Create Thrall, you can create one additional thrall in range.

[[srd/pf2e/compendium/character/Grim Fascinations#Spirit|**Spirit**]] *Level 1*

`necromancer`

Spirit necromancers, also known as vitamancers, seek the secrets of the soul and play with the eternal energies of the living and dead. Your thralls often resemble ghosts and spirits.

**Grave Spell** Life Tap

**Thrall Enhancement** Your thralls, while still being tied to the physical world, have an incorporeal essence. Whenever one of your thralls Strikes, you can choose for that damage to be spirit or void damage instead of physical damage.

[[srd/pf2e/compendium/character/class-features/necromancer/Undead Lore|**Undead Lore**]] *Level 1*

`necromancer`

Your dealings with death have expanded your knowledge of the macabre. You know the dead and what they are capable of. You become trained in Undead Lore, a special lore skill that can be used to Recall Knowledge regarding undead creatures, haunts, and effects caused by undead creatures or other necromancers, but that can't be used to Recall Knowledge of other topics. At 3rd level, you become an expert in Undead Lore; at 7th level, you become a master in Undead Lore; and at 15th level, you become legendary in Undead Lore.

### Class Feats

[[srd/pf2e/compendium/spells/focus/Muscle Barrier|**Muscle Barrier**]] *Level 2*

`necromancer`

You create an extra thick layer of muscle to protect your target. You learn the Muscle Barrier grave spell.

[[srd/pf2e/compendium/feats/howl-of-the-wild/archetype/Winged Warrior Dedication|**Winged Warrior Dedication**]] *Level 2*

`archetype`  `dedication`

Through rigorous training, you have strengthened your wings, granting you enough thrust to gain additional altitude. When you make a horizontal Leap, increase the distance by 10 feet up to a maximum of your Speed. Any fly Speed granted by ancestry feats and other permanent wings increases by 5 feet.

Winged Warrior

### Ancestry Features

**Animal Attack** *Level 1*

Your heritage gives you a special unarmed attack instead of the fist unarmed attack humanoids typically gain. This attack is in the brawling weapon group. Work with your GM to determine which one you have, using the type of animal you are and suggestions in your heritage for guidance. For example, you might choose a beak, talon, or wing for an eagle, a fist or tail for a monkey, or a tongue or jaws for a toad.
Unarmed AttackDamageTraits**Antler**1d6 PFinesse, unarmed**Beak**1d6 PFinesse, unarmed**Claw**1d4 SAgile, finesse, unarmed**Fangs**1d6 PFinesse, unarmed**Fist**1d4 BAgile, finesse, nonlethal, unarmed**Horn**1d6 PFinesse, unarmed**Jaws**1d6 PFinesse, unarmed**Tail**1d6 BFinesse, trip, unarmed**Talon**1d4 PAgile, finesse, unarmed**Tongue**1d6 BFinesse, unarmed**Wing**1d4 BAgile, finesse, unarmed

**Awakened Form** *Level 1*

Awakening altered your form, enabling you to speak verbally and stand on two legs. You can wear, hold, wield, and use items. Which limbs you use to manipulate items and how many are determined by you and your GM, but for the rules you function like a humanoid with two hands.

**Awakened Mind** *Level 1*

Awakening altered your mind. You are no longer an animal, but you can still ask questions of, receive answers from, and use the Diplomacy skill with animals of your kind. By remembering your instincts, you can allow yourself to be affected by spells and other effects as though you were an animal.

### Ancestry Feats

[[srd/pf2e/compendium/feats/howl-of-the-wild/ancestry/Awakened Magic|**Awakened Magic**]] *Level 1*

`awakened-animal`

When you awakened, primal magic was released within you. Choose one cantrip from the primal spell list. You can cast this spell as an primal innate spell at will. A cantrip is heightened to a spell rank equal to half your level rounded up.

### Skill Feats

[[srd/pf2e/compendium/feats/player-core/skill/Battle Medicine|**Battle Medicine**]] *Level 1*

`general`  `healing`  `manipulate`  `skill`

**Requirements** You're holding or wearing a healer's toolkit.

You can patch up wounds, even in combat. Attempt a Medicine check with the same DC as for Treat Wounds and restore the corresponding amount of HP; this doesn't remove the wounded condition. As with Treat Wounds, you can attempt checks against higher DCs if you have the minimum proficiency rank. The target is then immune to your Battle Medicine for 1 day. This does not make them immune to, or otherwise count as, Treat Wounds.


## Inventory

### Currency

| Denomination | Qty |
|---|---|
| Silver (sp) | 3 |
| **Total** | **0.30 gp** |

### Worn and Invested

| Item | Qty | Bulk | Price |
|---|---|---|---|
| [[srd/pf2e/compendium/equipment/armor#Kilted Breastplate\|Kilted Breastplate]] |  | 1 | 3 gp |
| Psychopomp Mask |  |  | 5 gp |
| [[srd/pf2e/compendium/equipment/worn-items/Ring of Sigils\|Ring of Sigils]] |  |  | 20 gp |

### Carried

| Item | Qty | Bulk | Price |
|---|---|---|---|
| [[srd/pf2e/compendium/equipment/adventuring-gear/backpack\|Backpack]] |  |  | 1 sp |
| [[srd/pf2e/compendium/equipment/adventuring-gear/bedroll\|Bedroll]] |  | 0.1 | 2 cp |
| [[srd/pf2e/compendium/equipment/adventuring-gear/chalk\|Chalk]] | 10 |  | 1 cp |
| [[srd/pf2e/compendium/equipment/adventuring-gear/Flint and Steel\|Flint and Steel]] |  |  | 5 cp |
| [[srd/pf2e/compendium/equipment/adventuring-gear/Healer's Toolkit\|Healer's Toolkit]] |  | 1 | 5 gp |
| Healing Potion (Minor) |  | 0.1 | 4 gp |
| Lover's Knot |  |  | 6 gp |
| [[srd/pf2e/compendium/equipment/armor#Padded Armor\|Padded Armor]] |  | 0.1 | 2 sp |
| [[srd/pf2e/compendium/equipment/adventuring-gear/rations\|Rations]] | 2 | 0.1 | 4 sp |
| [[srd/pf2e/compendium/equipment/adventuring-gear/rope\|Rope]] |  | 0.1 | 5 sp |
| [[srd/pf2e/compendium/equipment/adventuring-gear/soap\|Soap]] |  |  | 2 cp |
| [[srd/pf2e/compendium/equipment/adventuring-gear/torch\|Torch]] | 5 | 0.1 | 1 cp |
| [[srd/pf2e/compendium/equipment/adventuring-gear/waterskin\|Waterskin]] |  | 0.1 | 5 cp |
