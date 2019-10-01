#!/bin/bash

HTML_BUILD_PATH=_build/html/
SOURCE_DOCS_DIR=_sources
PROVIDER_DOCS_DIR=provider-docs
PROVIDERS_DIR=providers
GENERATED_DOC_PATH=build/docs/javadoc

generate() {
    echo "Generating documentation for $1"

    PROVIDER_DIR=`basename -s .git $1`

    if [ -d $PROVIDER_DIR ]; then
        rm -rf $PROVIDER_DIR
    fi

    git clone -b bug/fix-documentation $1
    cd $PROVIDER_DIR

    touch settings.gradle
    ./gradlew referenceDocs

    PROVIDER_DIR_PATH=$(pwd)

    cd -

    PROVIDER=$(echo ${PROVIDER_DIR} | sed -e 's/gyro-\(.*\)-provider/\1/')

    cd ..

    cd $PROVIDERS_DIR

    if [ -d $PROVIDER ]; then
        rm -rf $PROVIDER
    fi

    mkdir -p $PROVIDER

    cp -a $PROVIDER_DIR_PATH"/"$GENERATED_DOC_PATH"/" $(pwd)"/"$PROVIDER

    cd ../$PROVIDER_DOCS_DIR
}

mkdir -p $PROVIDER_DOCS_DIR && cd $PROVIDER_DOCS_DIR

for provider in `cat ../providers.txt`;
do
    generate $provider
done

cd ..

rm -rf $PROVIDER_DOCS_DIR $HTML_BUILD_PATH$PROVIDER_DOCS_DIR $HTML_BUILD_PATH$SOURCE_DOCS_DIR
