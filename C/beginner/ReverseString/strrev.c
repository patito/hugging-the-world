#include <stdio.h>
#include <string.h>

#include <CUnit/Basic.h>
#include <CUnit/CUnit.h>

static void strrev(char *str)
{
    if ((NULL == str) || ('\0' == *str)) return; 
	char *end_str = str + strlen(str) - 1;
    
    while(end_str > str) {
        char c = *str;
        *str = *end_str;
        *end_str = c;
        end_str--;
        str++;
    }
}

static void strrev_TEST()
{
    char str[] = "Linux";
  
    strrev(NULL);
    CU_ASSERT(0 == strncmp(str, "Linux", 5));
    CU_ASSERT(-1 == strncmp(str, "xuniL", 5));

    strrev(str); 
    CU_ASSERT(0 == strncmp(str, "xuniL", 5));
    CU_ASSERT(-1 == strncmp(str, "xunil", 5));
    CU_ASSERT(1 == strncmp(str, "xunIL", 5));
}

CU_ErrorCode strrev_test_suite(CU_pSuite *rsuite)
{
    CU_pSuite suite = NULL;

    if (NULL == rsuite) {
        return -1;
    }

    suite = CU_add_suite("strrev", NULL, NULL);
    if (NULL == suite) {
        *rsuite = NULL;
        return CU_get_error();
    }

    if (NULL == CU_add_test(suite, "strrev_TEST", strrev_TEST)) {
        *rsuite = NULL;
        return CU_get_error();
    }

    *rsuite = suite;
    return CUE_SUCCESS;
}


int main()
{
    CU_pSuite strrev_suite = NULL;

    /* initialize the CUnit test registry */
    if (CUE_SUCCESS != CU_initialize_registry()) {
        return CU_get_error();
    }

    /* add a suite to the registry */
    if (CUE_SUCCESS != strrev_test_suite(&strrev_suite)) {
        fprintf(stderr, "Failed to create test suite.\n");
        CU_cleanup_registry();
        return 1;
    }

    /* Run all tests using the CUnit Basic interface */
    CU_basic_set_mode(CU_BRM_VERBOSE);
    CU_basic_run_tests();

    if (CU_get_number_of_tests_failed() > 0) {
        CU_cleanup_registry();
        return 1;
    }

    return 0;
}
