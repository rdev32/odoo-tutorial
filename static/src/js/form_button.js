/** @odoo-module */
import { FormController } from "@web/views/form/form_controller";
import { formView } from "@web/views/form/form_view";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

export class CustomButtonController extends FormController {
  setup() {
    super.setup();
    this.actionService = useService("action");
  }

  OnSaveItem() {
    this.actionService.doAction({
      type: "ir.actions.act_window",
      res_model: "estate.property",
      name: "Item created",
      view_mode: "form", // modal
      view_type: "form",
      views: [[false, "form"]],
      target: "new", //"current",
      res_id: false,
    });
  }

  OnDeleteItem() {
    this.actionService.doAction({
      type: "ir.actions.act_window",
      res_model: "estate.property",
      name: `Delete `,
      view_mode: "form",
      view_type: "form",
      views: [[false, "form"]],
      target: "new",
      res_id: false// find a way to get the id of the current item,
    });
  }
}

CustomButtonController.template = "button_estate.FormView.Buttons";

export const modelInfoView = {
  ...formView,
  Controller: CustomButtonController,
};

registry.category("views").add("buttons_in_form", modelInfoView);
