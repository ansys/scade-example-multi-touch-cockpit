#include "sgl.h"

/* Imported functions */

void disableTextPosAdjustment(void){
	sglDisable(SGL_TEXT_POS_ADJUSTMENT);
}


void enableTextPosAdjustment(void){
	sglEnable(SGL_TEXT_POS_ADJUSTMENT);
}
