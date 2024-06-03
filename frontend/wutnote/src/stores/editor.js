import { Extension } from '@tiptap/core';

const FontSize = Extension.create({
  name: 'font-size',

  addOptions() {
    return {
      fontSizes: ['12px', '14px', '16px', '18px', '20px', '24px'],
    };
  },

  addCommands() {
    return {
      increaseFontSize: () => {
        return this.editor.commands.setNode(({
          type: 'text',
          attrs: {
            fontSize: this.editor.getAttributes('fontSize').fontSize ? this.editor.getAttributes('fontSize').fontSize + 1 : 1,
          },
        }));
      },
      decreaseFontSize: () => {
        return this.editor.commands.setNode(({
          type: 'text',
          attrs: {
            fontSize: this.editor.getAttributes('fontSize').fontSize && this.editor.getAttributes('fontSize').fontSize > 1 ? this.editor.getAttributes('fontSize').fontSize - 1 : this.editor.getAttributes('fontSize').fontSize,
          },
        }));
      },
    };
  },
});
