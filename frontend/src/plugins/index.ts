import PrimeVue from 'primevue/config';
import Aura from '@primeuix/themes/aura';

import Button from "primevue/button";
import Badge from 'primevue/badge';
import ScrollPanel from 'primevue/scrollpanel';
import Tooltip from 'primevue/tooltip';
import Textarea from 'primevue/textarea';
import FloatLabel from 'primevue/floatlabel';
import Carousel from 'primevue/carousel';
import Dialog from 'primevue/dialog';

export default function setupPrimevue(app: any){
    app.use(PrimeVue, {
    theme: {
        preset: Aura
    }
})
    app.component("PrimevueButton", Button)
    app.component("PrimevueBadge", Badge)
    app.component("PrimevueScrollPanel", ScrollPanel)
    app.component("PrimevueFloatLabel", FloatLabel)
    app.component("PrimevueTextarea", Textarea)
    app.component("PrimevueCarousel", Carousel)
    app.component("PrimevueDialog", Dialog)
    app.directive('tooltip', Tooltip);
}