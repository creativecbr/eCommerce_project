<?php
/* Smarty version 3.1.33, created on 2020-11-12 23:10:37
  from '/var/www/html/admubrokeit/themes/default/template/content.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.33',
  'unifunc' => 'content_5fadb2dd7109c2_96223519',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '358b2beb4116fc81c5f97e244a1930332d0df191' => 
    array (
      0 => '/var/www/html/admubrokeit/themes/default/template/content.tpl',
      1 => 1600952248,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_5fadb2dd7109c2_96223519 (Smarty_Internal_Template $_smarty_tpl) {
?><div id="ajax_confirmation" class="alert alert-success hide"></div>
<div id="ajaxBox" style="display:none"></div>


<div class="row">
	<div class="col-lg-12">
		<?php if (isset($_smarty_tpl->tpl_vars['content']->value)) {?>
			<?php echo $_smarty_tpl->tpl_vars['content']->value;?>

		<?php }?>
	</div>
</div>
<?php }
}
