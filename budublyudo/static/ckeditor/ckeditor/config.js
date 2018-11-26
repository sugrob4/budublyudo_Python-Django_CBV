/**
 * @license Copyright (c) 2003-2018, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see https://ckeditor.com/legal/ckeditor-oss-license
 */

CKEDITOR.editorConfig = function( config ) {
    config.language = 'ru';
    config.toolbarCanCollapse = true;
    config.forcePasteAsPlainText = true;
    config.enterMode = CKEDITOR.ENTER_BR;
    config.indentClasses = ["ul-grey", "ul-red", "text-red", "ul-content-red", "circle", "style-none", "decimal", "paragraph-portfolio-top", "ul-portfolio-top", "url-portfolio-top", "text-grey"];
    config.protectedSource.push(/<(style)[^>]*>.*<\/style>/ig);
    config.protectedSource.push(/<(script)[^>]*>.*<\/script>/ig);// разрешить теги <script>
    config.protectedSource.push(/<(i)[^>]*>.*<\/i>/ig);// разрешить теги <i>
    config.protectedSource.push(/<!--dev-->[\s\S]*<!--\/dev-->/g);
    config.protectedSource.push(/<[a-z]*[a-z\s="']*><\/[\s\S][^/]*?>/g);
    config.allowedContent = true; /* all tags */
};
