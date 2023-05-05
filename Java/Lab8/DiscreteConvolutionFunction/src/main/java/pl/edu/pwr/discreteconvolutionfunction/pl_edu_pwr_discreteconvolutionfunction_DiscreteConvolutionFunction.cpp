#include<jni.h>
#include "pl_edu_pwr_discreteconvolutionfunction_DiscreteConvolutionFunction.h"

JNIEXPORT jobjectArray JNICALL Java_pl_edu_pwr_discreteconvolutionfunction_DiscreteConvolutionFunction_calculateDiscreteConvolutionFunctionNative
(JNIEnv* env, jobject obj, jobjectArray data, jobjectArray kernel) {
	int data_size = env->GetArrayLength(data);
	int kernel_size = env->GetArrayLength(kernel);
	int result_size = data_size - kernel_size + 1;
	//create flipped kernel
	int** flipped_kernel = new int* [kernel_size];
	for (int i = 0; i < kernel_size; i++) {
		flipped_kernel[i] = new int[kernel_size];
	}
	//write elements to flipped kernel
	jintArray kernel_inner_array;
	jint* kernel_buffer;
	jint tmp[1];
	for (int i = 0; i < kernel_size; i++) {
		kernel_inner_array = (jintArray)env->GetObjectArrayElement(kernel, kernel_size - 1 - i);
		kernel_buffer = env->GetIntArrayElements(kernel_inner_array, NULL);
		for (int j = 0; j < kernel_size; j++) {
			tmp[0] = (int)kernel_buffer[kernel_size - 1 - j];
			flipped_kernel[i][j] = tmp[0];
		}
	}
	//create data copy
	int** data_copy = new int* [data_size];
	for (int i = 0; i < data_size; i++) {
		data_copy[i] = new int[data_size];
	}
	//write elements to data copy
	jintArray data_inner_array;
	jint* data_buffer;
	for (int i = 0; i < data_size; i++) {
		data_inner_array = (jintArray) env -> GetObjectArrayElement(data, i);
		data_buffer = env->GetIntArrayElements(data_inner_array, NULL);
		for (int j = 0; j < data_size; j++) {
			tmp[0] = (int)data_buffer[j];
			data_copy[i][j] = tmp[0];
		}
	}
	//creating result
	jclass cls = env->FindClass("[I");
	jintArray initTable = env->NewIntArray(result_size);
	jobjectArray result = env->NewObjectArray(result_size, cls, initTable);
	jintArray innerArray;
	jint sum[1] = { 0 };
	for (int i = 0; i < result_size; i++) {
		innerArray = env->NewIntArray(result_size);
		for (int j = 0; j < result_size; j++) {
			sum[0] = 0;
			for (int k = 0; k < kernel_size; k++) {
				for (int l = 0; l < kernel_size; l++) {
					sum[0] += data_copy[i + k][j + l] * flipped_kernel[k][l];
				}
			}
			env->SetIntArrayRegion(innerArray, j, 1, sum);
		}
		env->SetObjectArrayElement(result, i, innerArray);
		env->DeleteLocalRef(innerArray);
	}
	//delete flipped kernel
	for (int i = 0; i < kernel_size; i++) {
		delete[] flipped_kernel[i];
	}
	delete[] flipped_kernel;
	//delete data copy
	for (int i = 0; i < data_size; i++) {
		delete[] data_copy[i];
	}
	delete[] data_copy;
	return result;
}
