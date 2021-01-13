<?php
/* Smarty version 3.1.33, created on 2021-01-13 21:06:46
  from '/var/www/html/themes/classic/templates/checkout/_partials/footer.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.33',
  'unifunc' => 'content_5fff52d60403c8_34480389',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    'ba536facb0cbfebfb2b4790329c0a3b528aee8c8' => 
    array (
      0 => '/var/www/html/themes/classic/templates/checkout/_partials/footer.tpl',
      1 => 1606086940,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_5fff52d60403c8_34480389 (Smarty_Internal_Template $_smarty_tpl) {
$_smarty_tpl->_loadInheritance();
$_smarty_tpl->inheritance->init($_smarty_tpl, false);
$_smarty_tpl->inheritance->instanceBlock($_smarty_tpl, 'Block_5544322525fff52d603ef73_84401775', 'footer');
?>

<?php }
/* {block 'footer'} */
class Block_5544322525fff52d603ef73_84401775 extends Smarty_Internal_Block
{
public $subBlocks = array (
  'footer' => 
  array (
    0 => 'Block_5544322525fff52d603ef73_84401775',
  ),
);
public function callBlock(Smarty_Internal_Template $_smarty_tpl) {
?>

<div class="text-sm-center">
  <?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'%copyright% %year% - Ecommerce software by %prestashop%','sprintf'=>array('%prestashop%'=>'PrestaShop™','%year%'=>date('Y'),'%copyright%'=>'©'),'d'=>'Shop.Theme.Global'),$_smarty_tpl ) );?>

</div>
<?php
}
}
/* {/block 'footer'} */
}
