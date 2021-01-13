<?php
/* Smarty version 3.1.33, created on 2021-01-13 20:55:34
  from '/var/www/html/admubrokeit/themes/new-theme/template/content.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.33',
  'unifunc' => 'content_5fff5036cffb09_10280284',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    'a990a70d2539b5fda364d4e065263f1d2d01d100' => 
    array (
      0 => '/var/www/html/admubrokeit/themes/new-theme/template/content.tpl',
      1 => 1606086415,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_5fff5036cffb09_10280284 (Smarty_Internal_Template $_smarty_tpl) {
?>
<div id="ajax_confirmation" class="alert alert-success" style="display: none;"></div>


<?php if (isset($_smarty_tpl->tpl_vars['content']->value)) {?>
  <?php echo $_smarty_tpl->tpl_vars['content']->value;?>

<?php }
}
}
